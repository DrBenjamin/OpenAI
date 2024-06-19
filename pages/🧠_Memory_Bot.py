##### `🧠_Memory_Bot.py`
##### Memory Bot Demo
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
import deepl

# Set up the Streamlit app layout
st.set_page_config(page_title="StreamlitChatMessageHistory", page_icon="🧠")
st.title("🧠 Memory Bot")
st.markdown("""
A basic example of using ChatGPT with `StreamlitChatMessageistory` to help LLMChain remember messages in a conversation.
The messages are stored in Session State across re-runs automatically. You can view the contents of Session State
in the expander below. View the
[source code for this app](https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/basic_memory.py).
""")

# DeepL function
def translate(input_text, target_language = "DE"):
  translator = deepl.Translator(st.secrets["deepl"]["key"])
  result = translator.translate_text(input_text, target_lang = target_language) 
  return str(result)

# Sidebar
sidebar = st.sidebar
with sidebar:
  st.markdown("### 🧠 Memory Bot")
  on = st.toggle("OpenAI ChatGPT", True)
  if not on:
    st.markdown("Local Server Configuration")
    url = st.text_input("URL:", value="http://localhost")
    port = st.number_input("Port:", value=1234, min_value=1, max_value=65535)

# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
if len(msgs.messages) == 0:
    msgs.add_ai_message("How can I help you?")

view_messages = st.expander("View the message contents in session state")

# Set up the LangChain, passing in Message History
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a medical doctor named Dr. Benjamin having a conversation with a patient."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

# Setting the LLM
if on:
  chain = prompt | ChatOpenAI(
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
if prompt := st.chat_input():
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