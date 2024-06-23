import streamlit as st
from streamlit_cropper import st_cropper
from openai import OpenAI
client = OpenAI(api_key=st.secrets['openai']['key'])
# OpenAI API Key
api_key = st.secrets['openai']['key']
from PIL import Image
import io
import base64

# Function to encode the image via url
response = None
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
    max_tokens=1024,
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
    max_tokens=1024,
  )
  return response.choices[0].message.content

# Function to crop image
@st.experimental_fragment
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
st.title("Was ist auf diesem Bild?")
prompt = st.text_input("Gib hier den Text ein, um die Frage anzupassen.", value = "Was ist auf dem Bild?")
image_url = st.text_input("Gib hier den Link zum Bild ein")
if image_url:
  st.image(image_url, caption = 'Remote Bild.', use_column_width = True)
  response = openai_url_request(prompt, image_url)
  
uploaded_file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "png"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  
  # Cropping the image
  cropped_img = cropping(image)
  response = openai_image_request(prompt, cropped_img)

try:
  st.write(response)
except Exception as e:
  st.write('Wähle eine der obigen Optionen.')
  print(e)
