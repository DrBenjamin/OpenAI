##### `OpenAI.py`
#### Loading needed Python libraries
import streamlit as st
import openai
import streamlit_scrollable_textbox as sty
import PyPDF2



#### Streamlit initial setup
st.set_page_config(
  page_title = "OpenAI",
  page_icon = "https://www.benbox.org/R/OpenAI.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)




#### Initialization of session states
## Session states
if ('model' not in st.session_state):
  st.session_state['model'] = "text-davinci-003"
  
  


#### Functions





#### Main program
### Reading PDF documents
## Model selection
pdf = st.selectbox(label = 'What PDF document to use?', options = ["LEAM.pdf", "LLM.pdf"], index = 0)

# creating a pdf reader object
reader = PyPDF2.PdfReader('LLM.pdf')

# print the number of pages in pdf file
st.write(len(reader.pages))

# print the text of the first page
sty.scrollableTextbox(response_answer[reader.pages[0].extract_text(), height = 128, border = True)



### OpenAI ChatGPT
## Model selection
model = st.selectbox(label = 'What model to use?', options = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001", "code-davinci-002"], index = 0)

# Show info about model and set variable costs
if model == "text-davinci-003":
  st.write(':green[Capability of this model:] Most capable GPT-3 model. Can do any task the other models can do, often with higher quality, longer output and better instruction-following. Also supports inserting completions within text.')
  cost_co_eff = 0.02
elif model == "text-curie-001":
  st.write(':green[Capability of this model:] Very capable, but faster and lower cost than Davinci.')
  cost_co_eff = 0.002
elif model == "text-babbage-001":
  st.write(':green[Capability of this model:] Capable of straightforward tasks, very fast, and lower cost.')
  cost_co_eff = 0.0005
elif model == "text-ada-001":
  st.write(':green[Capability of this model:] Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.')
  cost_co_eff = 0.0004
elif model == "code-davinci-002":
  st.write(':green[Capability of this model:] Most capable Codex model. It is particularly good at translating natural language to code. In addition to completing code, also supports inserting completions within code.')
  cost_co_eff = 0.02
else:
  cost_co_eff = 0.02


## Form (to prevent unessessary requests)
with st.form("OpenAI"):
  # Text input
  question = st.text_input('What question do you want to ask OpenAI Chat-GPT?')
  
  # Temperature selection
  temp = st.slider('Which temperature?', 0.0, 1.0, .3)
  
  
  # Tokens selection
  tokens = st.slider('Max tokens?', 1, 2024, 128)
   
    
  ## Submit button
  submitted = st.form_submit_button('Ask OpenAI')
  if submitted:
    # Set API key
    openai.api_key = "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"
    
    # Using ChatGPT from OpenAI
    response_answer = openai.Completion.create(model = model, prompt = question, temperature = temp, max_tokens = tokens, top_p = 1.0, frequency_penalty = 0.0, presence_penalty = 0.0)
    
    # Show answer
    sty.scrollableTextbox(response_answer['choices'][0]['text'], height = 128, border = True)
    
    # Show costs per query
    costs = float(response_answer['usage']['total_tokens']) / 1000 * cost_co_eff
    if costs >= 0.0001:
      st.write('Costs: ' + str(costs) + '$')
    else:
      st.write('Costs: < 0.0001$')
