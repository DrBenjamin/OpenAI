##### `🤗_Hugging_Face.py`
##### OpenAI ChatGPT Demo
##### Open-Source, hostet on https://github.com/DrBenjamin/OpenAI
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
import streamlit_scrollable_textbox as sty
import requests




#### Streamlit initial setup
st.set_page_config(
  page_title = "Hugging Face Models",
  page_icon = "images/Hugging_Face.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
) 




#### Initialization of session states
## QR Code session state
if ('qrcode' not in st.session_state):
  st.session_state['qrcode'] = False
  
  
  
  
#### Functions
### Function: query = Hugging Face gpt2
def query(payload):
	response = requests.post(API_URL, headers = headers, json = payload)
	return response.json()




#### Main program
with st.form('Hugging Face'):
  query_text = st.text_input(label = 'Question: ')
  
  
  ## Submit button
	submitted = st.form_submit_button('Submit')
	 if submitted:
	   API_URL = "https://api-inference.huggingface.co/models/gpt2"
	   headers = {"Authorization": st.secrets['hugging_face']['key']}
	   output = query({"inputs": query_text,})
	   if output[0]['generated_text'] is not None:
	     sty.scrollableTextbox(output[0]['generated_text'], height = 128, border = True)
