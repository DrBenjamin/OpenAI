##### `🤗 - Hugging_Face.py`
##### OpenAI ChatGPT Demo
##### Open-Source, hostet on https://github.com/DrBenjamin/OpenAI
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
import streamlit.components.v1 as stc
import requests




#### Streamlit initial setup
st.set_page_config(
  page_title = "Hugging Face Models",
  page_icon = "images/Hugging_Face.png",
  layout = "centered",
  initial_sidebar_state = "expanded",
  menu_items = { 
         'Get Help': st.secrets['custom']['menu_items_help'],
         'Report a bug': st.secrets['custom']['menu_items_bug'],
         'About': st.secrets['custom']['menu_items_about']
        }
) 




#### Initialization of session states
## QR Code session state
if ('qrcode' not in st.session_state):
  st.session_state['qrcode'] = False
  
  
  
  
#### Functions
### Function: generate_qrcode = QR Code generator
def generate_qrcode(data):
  # Encoding data using make() function
  image = qrcode.make(data)
  
  # Saving image as png in a buffer
  byteIO = io.BytesIO()
  image.save(byteIO, format = 'PNG')

  # Return qrcode
  return byteIO.getvalue()




#### Main program
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": st.secrets['hugging_face']['key']}

def query(payload):
	response = requests.post(API_URL, headers = headers, json = payload)
	return response.json()
	
#output = query({"inputs": "Can you please let us know more details about your ",})

query_text = st.text_input(label = 'Question: ')
output = query({"inputs": query_text,})
st.write(output[0]['generated_text'])
