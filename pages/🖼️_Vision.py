### `🖼️_Vision.py`
### Vision
### Open-Source, hosted on https://github.com/DrBenjamin/OpenAI
### Please reach out to drdrbenjamin@icloud.com for any questions
## Loading needed Python libraries
import streamlit as st
from streamlit_cropper import st_cropper
from openai import OpenAI
from mistralai import Mistral
import os
from PIL import Image
import io
import base64

# Sidebar
with st.sidebar:
    mistral = st.toggle("Mistral", value = True)

# AI APIs
if mistral:
    client = Mistral(api_key=st.secrets['mistral']['key'])
    model = "pixtral-12b-2409"
else:
    client = OpenAI(api_key=st.secrets['openai']['key'])
    model="gpt-4-turbo"

# Function to encode the image via url
response = None
def ai_url_request(system_text, prompt_text, image_url):
  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "system",
        "content": [{
            "type": "text",
            "text:": f"{system_text}"
            
        }],
        "role": "user",
        "content": [
          {
            "type": "text", 
            "text": f"{prompt_text}"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"{image_url}",
            },
          },
        ],
      }
    ],
    max_tokens=1024,
  )
  return response.choices[0].message.content

# Function to encode the image
def ai_image_request(system_text, prompt_text, image):
  image_bytes = io.BytesIO()
  image = image.convert("RGB")
  image.save(image_bytes, format='JPEG', quality=95)
  image_bytes = image_bytes.getvalue()
  base64_image = base64.b64encode(image_bytes).decode('utf-8')
  messages=[
      {
        "role": "system",
        "content": [{
            "type": "text",
            "text:": f"{system_text}"
        }],
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
    ]
  if mistral:
    response = client.chat.complete(
      model=f"{model}",
      messages=messages
    )
  else:
    response = client.chat.completions.create(
      model=f"{model}",
      messages=messages,
      max_tokens=1024
    )
  return response.choices[0].message.content

# Function to crop image
@st.fragment
def cropping(image):
  if image:
      # Get a cropped image from the frontend
      cropped_img = st_cropper(image, realtime_update = True, box_color = '#0000FF',
                               aspect_ratio = [1, 1], default_coords = (1, image.width - 1, 1, image.height - 2))
      
      # Manipulate cropped image at will
      st.write("Preview")
      _ = cropped_img.thumbnail((200,200))
      st.image(cropped_img, caption = 'Bearbeitetes Bild.')
      return cropped_img

# Image input
image_url = st.text_input("Gib hier den Link zum Bild ein")
if image_url:
    st.image(image_url, caption = 'Remote Bild.', use_column_width = True)
uploaded_file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Cropping the image
    cropped_img = cropping(image)

with st.form(key='image_form'):
    st.title("Was ist auf diesem Bild?")
    system = st.text_input("Systemtext", value = "Analysiere den Screenshot vom NAVIS KIS (Krankenhausinformationssystem). Achte insebsondere auf die roten Rahmen und extrahiere die im Rahmen hervorgehobenen Informationen wie z.B. `Fälle & Besuche`.")
    prompt = st.text_input("Gib hier den Text ein, um die Frage anzupassen.", value = "Was ist auf dem Bild?")
    submitted = st.form_submit_button("Absenden")
    if submitted:
        try:
            if image_url:
                response = ai_url_request(system, prompt, image_url)
            if uploaded_file:
                response = ai_image_request(system, prompt, cropped_img)
            st.write(response)
        except Exception as e:
            st.write('Wähle eine der obigen Optionen.')
            print(e)
