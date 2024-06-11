import streamlit as st
from streamlit_cropper import st_cropper
from st_audiorec import st_audiorec
from openai import OpenAI
client = OpenAI(api_key=st.secrets['openai']['key'])
# OpenAI API Key
api_key = st.secrets['openai']['key']
from PIL import Image
import io
import base64
from pathlib import Path
from pydub import AudioSegment
#pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg/bin"

# Function to encode the image
def openai_request(text, image, transcription):
  image_bytes = io.BytesIO()
  image = image.convert("RGB")
  image.save(image_bytes, format='JPEG')
  image_bytes = image_bytes.getvalue()
  base64_image = base64.b64encode(image_bytes).decode('utf-8')
  
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text", 
            "text": f"{text}"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          },
          {
            "type": "text",
            "text": f"Hier ist noch die Beschreibung vom Nutzer: {transcription}"
          }
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
uploaded_file = st.file_uploader("Wähle ein Bild zum Hochladen aus", type=["jpg", "png"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  
  # Cropping the image
  cropped_img = cropping(image)

# Audio input
audio_transcription = ""
uploaded_audio_file = st.file_uploader("Wähle eine Sprachaufnahme zum Hochladen aus", type=["mp3"])
if uploaded_audio_file is not None:
  # Transcribe the audio
  audio_transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=uploaded_audio_file
  )
st.write("or record it here")
try:
  wav_audio_data = st_audiorec()
except:
  wav_audio_data = None
try:
  if wav_audio_data is not None:
      # Wav to mp3 conversion
      audio_data_io = io.BytesIO(wav_audio_data)
      audio = AudioSegment.from_wav(audio_data_io)
      mp3_audio_data = io.BytesIO()
      mp3_audio_data.name = "speech.mp3"
      audio.export(mp3_audio_data, format="mp3")
      audio_transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=mp3_audio_data
      )
except:
  audio_transcription = ""
  
# Start the analysis
button_pressed = st.button("Starte die Analyse")
if button_pressed:
  st.write("Analyse wird gestartet...")
  response = openai_request(prompt, cropped_img, audio_transcription)
  st.write(response)
  audio = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=response
  )
  st.audio(audio.read(), format="audio/mp3")
