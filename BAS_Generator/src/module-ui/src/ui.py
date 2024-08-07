def run_streamlit():
    ##### `ui.py`
    ##### BAS Anzeigen Generator
    ##### Please reach out to benjamin.gross1@adesso.de for any questions
    #### Loading needed Python libraries
    import streamlit as st
    import pandas as pd
    from snowflake.snowpark.functions import call_udf, col
    from snowflake.snowpark import Session

    # Get the current credentials
    session = Session.builder.getOrCreate()
    
    # Header
    st.title('❄️ BAS Anzeigen Generator')
    st.header('Generiere ein BAS Anzeigen Dokument')
    version = session.call('core.py_version')
    st.write(f"Python Version: {version}")
    st.write(f"Streamlit Version: {st.__version__}")
    
    # Establish Snowflake session
    @st.cache_resource
    def create_session():
        return Session.builder.configs(st.secrets.snowflake).create()

    session = create_session()
    st.success("Datenbankverbindung erfolgreich hergestellt.")

    # Load data table
    @st.cache_data
    def load_data(table_name):
        # Read in data table
        st.write(f"Beispieldaten von `{table_name}`:")
        table = session.table(table_name)
        
        # Do some computation on it
        table = table.limit(100)
        
        # Collect the results. This will run the query and download the data
        table = table.collect()
        return pd.DataFrame(table)

    # Select and display data table
    table_name = "BAS.PUBLIC.ANZEIGE_PRE"

    # Display data table
    with st.expander("Datenbankinhalt"):
        df = load_data(table_name)
        st.dataframe(df)
        
    # Sidebar
    sidebar = st.sidebar
    with sidebar:
      kunde = st.text_input("Anbieter:", value="GWQ ServicePlus AG")
      cloud = st.selectbox("Cloud:", ["AWS", "Azure", "Google Cloud"], index=2)
      on = st.toggle("OpenAI ChatGPT", True)
      system = st.text_input("System:", value = f"Du erstellst einzelne Absätze einer Anzeige beim Bundesamt für Soziale Sicherung über die Verarbeitung von Sozialdaten im Auftrag (AVV) nach § 80 Zehntes Sozialgesetzbuch (SGB X). Tausche <Variabel_Name> durch die entsprechenden Inhalte aus und gebe nur den Text aus und verzichte auf Phrasen wie z.B. 'Vielen Dank für die Informationen. Hier sind die angepassten Absätze für die Anzeige beim Bundesamt für Soziale Sicherung:'.")
      if not on:
        st.markdown("Local Server Configuration")
        url = st.text_input("URL:", value="http://localhost")
        port = st.number_input("Port:", value=1234, min_value=1, max_value=65535)

    # Set up memory
    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    if len(msgs.messages) == 0:
        msgs.add_ai_message(f"""Ich ersetze <Kunde> mit {kunde}, 
                              <Cloud-Anbieter> mit {cloud}.""")

    view_messages = st.expander("Zeige mir die Paragraphen an")

    # Set up the LangChain, passing in Message History
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", f"{system}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    # Setting the LLM
    if on:
      chain = prompt | ChatOpenAI(
        model="gpt-4o-mini",
        api_key=st.secrets["openai"]["key"]
      ) 
    else:
      server_url = f"{url}:{str(port)}/v1"
      chain = prompt | ChatOpenAI(
        base_url=server_url,
        model="llama-3-8b-chat-doctor-Q4_K_M_v2",
        temperature=0.5,
        max_tokens=4000,
        api_key="lm-studio"
      )

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="history",
    )

    # Render current messages from StreamlitChatMessageHistory
    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content)

    # If user inputs a new prompt, generate and draw a new response
    #if prompt := st.chat_input():
    for prompt in df["PARAGRAPH_TEXT"]:
        st.chat_message("human").write(prompt)
        # Note: new messages are saved to history automatically by Langchain during run
        config = {"configurable": {"session_id": "any"}}
        response = chain_with_history.invoke({"question": prompt}, config)
        st.chat_message("ai").write(response.content)

    # Draw the messages at the end, so newly generated ones show up immediately
    with view_messages:
        """
        Message History initialized with:
        ```python
        msgs = StreamlitChatMessageHistory(key="langchain_messages")
        ```

        Contents of `st.session_state.langchain_messages`:
        """
        view_messages.json(st.session_state.langchain_messages)

    # Convert to dataframe
    messages = st.session_state.langchain_messages
    anzeige_temp = pd.DataFrame(columns=['PARAGRAPH', 'PARAGRAPH_TEXT'])
    counter = -1
    paragraph = -1
    for index, message in enumerate(messages):
        for key, value in message:
            if key == "content":
                counter += 1
                if counter > 0 and counter % 2 == 0:
                    paragraph += 1
                    anzeige_temp = anzeige_temp._append(pd.DataFrame([{'PARAGRAPH': df['PARAGRAPH'][paragraph], 'PARAGRAPH_TEXT': value}]), ignore_index=True)

    st.dataframe(anzeige_temp)

if __name__ == '__main__':
    run_streamlit()
