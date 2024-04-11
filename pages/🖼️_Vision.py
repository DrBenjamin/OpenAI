import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets['openai']['key'])
# OpenAI API Key
api_key = st.secrets['openai']['key']
from PIL import Image
import io
import base64

# Function to encode the image via url
def openai_url_request(prompt_text, image_url):
  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text", 
            "text": f"{prompt_text}"
          },
          {
            "type": "image_url",
            "image_url": {
              "url":f"{image_url}",
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )
  return response.choices[0].message.content

# Function to encode the image
def openai_image_request(prompt_text, image):
  image_bytes = io.BytesIO()
  image = image.convert("RGB")
  image.save(image_bytes, format='JPEG')
  image_bytes = image_bytes.getvalue()
  base64_image = base64.b64encode(image_bytes).decode('utf-8')
  
  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text", 
            "text": f"{prompt_text}"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          },
        ],
      }
    ],
    max_tokens=300,
  )
  return response.choices[0].message.content

# Image input
st.title("Was ist auf diesem Bild?")
prompt = st.text_input("Gib hier den Text ein, um die Frage anzupassen.", value = "Was ist auf dem Bild?")
image_url = st.text_input("Gib hier den Link zum Bild ein")
if image_url:
  st.image(image_url, caption = 'Remote Bild.', use_column_width = True)
  response = openai_url_request(prompt, image_url)
  
uploaded_file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "png"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption = 'Hochgeladenes Bild.', use_column_width = True)
  response = openai_image_request(prompt, image)

try:
  st.write(response)
except Exception as e:
  st.write('Wähle eine der obigen Optionen.')
  print(e)
