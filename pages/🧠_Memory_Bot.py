##### `🧠_Memory_Bot.py`
##### Memory Bot Demo
##### https://medium.com/@avra42/how-to-build-a-chatbot-with-chatgpt-api-and-a-conversational-memory-in-python-8d856cda4542
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import OpenAI




#### Streamlit initial setup
st.set_page_config(
    page_title = "🧠 Memory Bot",
    page_icon = "images/Logo.png",
    layout = "centered",
    initial_sidebar_state = "expanded"
)




#### Session states
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []
   



#### Functions
### Function get_text = Get the user input
def get_text():
    """
    Get the user input text.
    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], key = "input",
                            placeholder = "Your AI assistant here! Ask me anything ...",
                            label_visibility = 'hidden')
    return input_text



### Function new_chat = clear session state and starts a new chat
def new_chat():
    """
    Clears session state and starts a new chat.
    """
    save = []
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        save.append("User:" + st.session_state["past"][i])
        save.append("Bot:" + st.session_state["generated"][i])
    st.session_state["stored_session"].append(save)
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["input"] = ""
    st.session_state.entity_memory.store = {}
    st.session_state.entity_memory.buffer.clear()




#### Main
with st.sidebar.expander(" 🛠️ Settings ", expanded = False):
    # Option to preview memory store
    if st.checkbox("Preview memory store"):
        st.write(st.session_state.entity_memory.store)
    # Option to preview memory buffer
    if st.checkbox("Preview memory buffer"):
        st.write(st.session_state.entity_memory.buffer)
    MODEL = st.selectbox(label = 'Model', options = ['gpt-3.5-turbo', 'text-davinci-003'])
    K = st.number_input(' (#)Summary of prompts to consider', min_value = 3,max_value = 1000)

# Set up the Streamlit app layout
st.title("🧠 Memory Bot")
st.markdown(
        '''
        :black[**A Chatbot that remembers,**  *powered by -  [LangChain]('https://langchain.readthedocs.io/en/latest/modules/memory.html#memory') +
        [OpenAI]('https://platform.openai.com/docs/models/gpt-3-5') +
        [Streamlit]('https://streamlit.io') + [DataButton](https://www.databutton.io/)*]
        ''')

# Get the OpenAI API key from secrets file
API_O = st.secrets['openai']['key']

# Create an OpenAI instance
llm = OpenAI(temperature = 0, openai_api_key = API_O, model_name = MODEL, verbose = False)

# Create a ConversationEntityMemory object if not already created
if 'entity_memory' not in st.session_state:
    st.session_state.entity_memory = ConversationEntityMemory(llm = llm, k = K)
    
# Create the ConversationChain object with the specified configuration
Conversation = ConversationChain(llm = llm, prompt = ENTITY_MEMORY_CONVERSATION_TEMPLATE, memory = st.session_state.entity_memory)
st.sidebar.button("New Chat", on_click = new_chat, type = 'primary')
user_input = get_text()
if user_input:
    output = Conversation.run(input=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Allow to download as well
download_str = []
# Display the conversation history using an expander, and allow the user to download it
with st.expander("Conversation", expanded = True):
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        st.info(st.session_state["past"][i], icon = "🧐")
        st.success(st.session_state["generated"][i], icon = "🤖")
        download_str.append(st.session_state["past"][i])
        download_str.append(st.session_state["generated"][i])
    
    # Can throw error - requires fix
    download_str = '\n'.join(download_str)
    if download_str:
        st.download_button('Download', download_str)
        
# Display stored conversation sessions in the sidebar
for i, sublist in enumerate(st.session_state.stored_session):
        with st.sidebar.expander(label= f"Conversation-Session:{i}"):
            st.write(sublist)

# Allow the user to clear all stored conversation sessions
if st.session_state.stored_session:
    if st.sidebar.checkbox("Clear-all"):
        del st.session_state.stored_session