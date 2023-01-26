##### `OpenAI.py`
#### Loading needed Python libraries
import streamlit as st
import streamlit_scrollable_textbox as sty
import openai
import PyPDF2
import os




#### Streamlit initial setup
st.set_page_config(
  page_title = "OpenAI",
  page_icon = "https://www.benbox.org/R/OpenAI.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)
  
  


#### Main program
st.header('OpenAI ChatGPT Playground')
answer = ''
used_tokens = 0
### PDF documents
st.subheader('Use data from a PDF source')
pdf_text = ' "'
index = 0
pdf_usage = st.checkbox('Include a PDF source to feed ChatGPT with data?')
if pdf_usage:
	st.write('**:green[Use your own PDF]**')
	documents = ["LEAM.pdf", "LLM.pdf", "KW.pdf", "AIDH.pdf", "PC.pdf"]
	uploaded_file = st.file_uploader(label = 'Choose a PDF file to upload', type = 'pdf')
	if uploaded_file is not None:
		file_name = os.path.join('PDFs', uploaded_file.name)
		file = open(file_name, 'wb')
		file.write(uploaded_file.getvalue())
		file.close()
		documents.append(uploaded_file.name)
		index = 4
	
	
	## Source selection
	st.write('**:green[or a provided PDF about AI / Programming]**')
	pdf = st.selectbox(label = 'Choose PDF document?', options = documents, index = index)
	
	# Creating a pdf reader object
	reader = PyPDF2.PdfReader('PDFs/' + pdf)
	
	# Select pages
	if len(reader.pages) > 1:
		pages_range = st.slider(label = 'Select a range of pages you want to use for the dialog with ChatGPT', min_value = 1, max_value = len(reader.pages), value = (1, 1))
	
		# print the text of the first page
		pagez = []
		for i in range(pages_range[0], pages_range[1], 1):
			pagez.append(i)
			pdf_text += reader.pages[i].extract_text()
		pdf_text += '"'
		page = st.radio(label = 'Page preview for selecting meaningful pages of the PDF source (use slider above to adjust)', options = pagez, horizontal = True, index = 0)
		if page is None:
			page = 0
		sty.scrollableTextbox(reader.pages[page].extract_text(), height = 256, border = True)
	else:
		sty.scrollableTextbox(reader.pages[0].extract_text(), height = 256, border = True)



### OpenAI ChatGPT
## Model selection
st.subheader('Choose a model')
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


col1, col2 = st.columns(2)

with col1:
	## Form (to prevent unessessary requests)
	with st.form("OpenAI"):
	  # Text input
	  st.subheader('Communicate')
	  question = st.text_input('What question do you want to ask OpenAI Chat-GPT?')
	  
	  # Temperature selection
	  temp = st.slider('Which temperature?', 0.0, 1.0, .3)
	  
	  
	  # Tokens selection
	  tokens = st.slider("Answer's max tokens", 1, 1024, 128)
	   
	    
	  ## Submit button
	  submitted = st.form_submit_button('Submit')
	  if submitted:
	    # Set API key
	    openai.api_key = st.secrets['openai']['key']
	    
	    # Using ChatGPT from OpenAI
	    response_answer = openai.Completion.create(model = model, prompt = question + pdf_text, temperature = temp, max_tokens = tokens, top_p = 1.0, frequency_penalty = 0.0, presence_penalty = 0.0)
	    answer = response_answer['choices'][0]['text']
	    used_tokens = response_answer['usage']['total_tokens']

with col2:
	st.subheader('Examples')
	if pdf_usage:
		if model != "code-davinci-002":
			st.markdown('If you included PDF data type in something like\n\n*:orange[Please summarise this:]*\n\nor\n\n*:orange[Summarise this in 5 sentences:]*')
		else:
			st.markdown('If you included PDF data and choosen "Code-Davinci" model you can type in something like\n\n*:orange[Write a Python program to use ChatGPT like this:]*')
	elif model == "code-davinci-002":
		st.markdown('If choosen "Code-Davinci" model you can type in something like\n\n*:orange[Please write an Python script to use OpenAI ChatGPT and print out the source code]*')
	elif model == "text-curie-001":
		st.markdown('If choosen "Curie" model you can type in something like\n\n*:orange[Extract a keyword in this text "Saturdays it is often raining!"]*')
	elif model == "text-babbage-001":
		st.markdown('If choosen "Babbage" model you can type in something like\n\n*:orange[Improve this text "Saturdays it is often raining!"]*')
	elif model == "text-ada-001":
		st.markdown('If choosen "Ada" model you can type in something like\n\n*:orange[Rephrase this text "Saturdays it is often raining!"]*')
	else:
		st.markdown('Type in something like\n\n*:orange[Write me a short poem] or :orange[What is the last newspaper you have read?]*')
	st.markdown('**Temperature**\n\n:green[*0 = each answer will be the same*]\n\n:green[*1 = more "creative" answers*]')
	st.markdown('**Tokens**\n\n:green[*1 token ~= 4 chars in English*]')
	

### Outside columns
## Show answer
if answer != '':
	sty.scrollableTextbox(answer, height = 128, border = True)
		    
	# Show costs per query
	costs = float(used_tokens) / 1000 * cost_co_eff
	if costs >= 0.0001:
		st.write(':red[Costs: ' + str(round(costs, 4)) + '$]')
	else:
		st.write(':red[Costs: < 0.0001$]')
