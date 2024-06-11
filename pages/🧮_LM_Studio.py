import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="StreamlitChatMessageHistory", page_icon="🧮")
st.title("🧮 LM Studio local model")

"""
A basic example of using a local hosted LLM with LM Studio. It uses `StreamlitChatMessageHistory` to help LLMChain 
remember messages in a conversation. The messages are stored in Session State across re-runs automatically. View the
[source code for this app](https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/basic_memory.py).
"""
    
msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(memory_key="history", chat_memory=msgs)
if len(msgs.messages) == 0:
    msgs.add_ai_message("How can I help you?")

view_messages = st.expander("View the message contents in session state")

template = """You are an AI chatbot having a conversation with a human.

{history}
Human: {human_input}
AI: """

prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)

# Setting the LLM
server_url = "http://localhost:1234/v1"
model = "" #"LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF"
llm = ChatOpenAI(
  base_url=server_url,
  model=model,
  temperature=0.5,
  max_tokens=4000
)
llm_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():
    st.chat_message("human").write(prompt)

    # New messages are added to `StreamlitChatMessageHistory` when the Chain is called
    response = llm_chain.run(prompt)
    st.chat_message("ai").write(response)
    
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