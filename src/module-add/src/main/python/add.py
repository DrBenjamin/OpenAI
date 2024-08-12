##### `add.py`
##### BAS Anzeigen Generator
##### Please reach out to benjamin.gross1@adesso.de for any questions
#### Loading needed Python libraries
import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# UDF
def add_fn(kunde: str, cloud: str, system: str, on: bool, openai_api_key: str, url: str, port: str) -> str:
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
        api_key=openai_api_key
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
    df = pd.DataFrame(
        {
            "PARAGRAPH": ["1.0"],
            "PARAGRAPH_TEXT": ["Die GWQ ServicePlus AG (GWQ) ist ein Dienstleister an der Schnittstelle zwischen Krankenkassen und den Erbringern medizinischer Versorgung."]
        }
    )
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
    return anzeige_temp
