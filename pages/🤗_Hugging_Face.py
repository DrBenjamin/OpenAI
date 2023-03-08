##### `🤗_Hugging_Face.py`
##### Diffuser Demo
##### https://pypi.org/project/diffusers/
##### https://huggingface.co/docs/diffusers/optimization/mps
#### Loading needed Python libraries
import streamlit as st
import numpy as np
import audio2numpy as a2n
from pydub import AudioSegment
import cv2
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
from diffusers import StableDiffusionImg2ImgPipeline
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from transformers import pipeline
from transformers import pipeline, set_seed
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from datasets import load_dataset
import os
os.environ['COMMANDLINE_ARGS'] = '--skip-torch-cuda-test --upcast-sampling --no-half-vae --no-half --use-cpu interrogate'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'




#### Streamlit initial setup
st.set_page_config(
  page_title = "Hugging Face Diffuser Models",
  page_icon = "images/Hugging_Face.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)




#### Functions
### Function predict_step = Image to Text recognition
def predict_step(image):
    if image.mode != "RGB":
        image = image.convert(mode = "RGB")
    pixel_values = feature_extractor(images = image, return_tensors = "pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens = True)
    preds = [pred.strip() for pred in preds]
    return str(preds[0]).capitalize() + '.'
    



#### Models
st.header('🤗 Hugging Face Diffusers')
st.write('State-of-the-art diffusion models for image, text and audio generation in PyTorch.')
devices = ["mps", "cpu", "cuda"]
device = st.selectbox(label = 'Select device', options = devices, index = 1, disabled = False)
models = ["runwayml/stable-diffusion-v1-5", "stabilityai/stable-diffusion-2-1", "hakurei/waifu-diffusion", "stabilityai/stable-diffusion-2-base", "nlpconnect/vit-gpt2-image-captioning", "openai-gpt", "gpt2-large", "openai/whisper-large-v2"]
model_id_or_path = st.selectbox(label = 'Select model', options = models)
control_net_models = ["None", "lllyasviel/sd-controlnet-canny", "lllyasviel/sd-controlnet-scribble"]
if model_id_or_path == "runwayml/stable-diffusion-v1-5":
    disable = False
else:
    disable = True
control_net_model = st.selectbox(label = 'Select control net model', options = control_net_models, disabled = disable)
if model_id_or_path != "runwayml/stable-diffusion-v1-5":
    control_net_model = "None"



  
#### Stable diffusion image 2 image with Control Net
if model_id_or_path == "runwayml/stable-diffusion-v1-5" and control_net_model != "None":
    with st.form('img2img (Control Net)'):
        st.subheader('Image 2 Image (Control Net)')
        image = ''
        uploaded_file = st.file_uploader(label = "Upload a picture", type = 'png')
        prompt = st.text_input(label = 'Prompt', value = 'A picture in comic style, bright colours, a house with red bricks, a dark sky with a full yellow moon, best quality, extremely detailed.')
        submitted = st.form_submit_button('Submit')
        if submitted:
            # Check for image data
            if uploaded_file is not None:
                image = cv2.imdecode(np.frombuffer(uploaded_file.getvalue(), np.uint8), cv2.COLOR_GRAY2BGR)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
                # Resize image if existend and not 768x640 / 640x768 pixel
                h, w = image.shape
                if not (h == 768 and w == 640) and not (h == 640 and w == 768):
                    # Image is bigger in height than width
                    if h > w:
                        # Resize cropped image to standard dimensions
                        image = cv2.resize(image, (640, 768), interpolation = cv2.INTER_AREA)
                
                    # Image is smaller in height than width
                    else:
                        # Resize cropped image to standard dimensions
                        image = cv2.resize(image, (768, 640), interpolation = cv2.INTER_AREA)
        
                # Get canny image
                image = cv2.Canny(image, 100, 200)
                image = image[:, :, None]
                image = np.concatenate([image, image, image], axis = 2)
                canny_image = Image.fromarray(image)
                st.subheader('Preview annotator result')
                st.image(canny_image)
        
            # Load control net and stable diffusion v1-5
            controlnet = ControlNetModel.from_pretrained(control_net_model, torch_dtype = torch.float16)
            pipe = StableDiffusionControlNetPipeline.from_pretrained(model_id_or_path, controlnet = controlnet, torch_dtype = torch.float16)
            pipe = pipe.to(device)
            
            # Recommended if your computer has < 64 GB of RAM
            pipe.enable_attention_slicing()
        
            # Speed up diffusion process with faster scheduler and memory optimization
            pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
            #pipe.enable_model_cpu_offload()
        
            # Generate image
            generator = torch.manual_seed(0)
            image = pipe(prompt = prompt, negative_prompt = "monochrome, lowres, bad anatomy, worst quality, low quality", num_inference_steps = 30, generator = generator, image = canny_image).images[0]
            st.subheader('Diffuser result')
            st.write('Model :orange[' + model_id_or_path + '] + :red[' + control_net_model + ']')
            st.image(image)


## Stable-Diffusion
if model_id_or_path == "runwayml/stable-diffusion-v1-5" and control_net_model == "None":
    with st.form('img2img'):
        st.subheader('Image 2 Image')
        image = ''
        uploaded_file = st.file_uploader(label = "Upload a picture", type = 'png')
        prompt = st.text_input(label = 'Prompt', value = 'A picture in comic style, bright colours, a house with red bricks, a dark sky with a full yellow moon, best quality, extremely detailed.')
        submitted = st.form_submit_button('Submit')
        if submitted:
            # Check for image data
            if uploaded_file is not None:
                image = cv2.imdecode(np.frombuffer(uploaded_file.getvalue(), np.uint8), cv2.IMREAD_COLOR)
                
                # Resize image if existend and not 768x640 / 640x768 pixel
                h, w, _ = image.shape
                if not (h == 768 and w == 640) and not (h == 640 and w == 768):
                    # Image is bigger in height than width
                    if h > w:
                        # Resize cropped image to standard dimensions
                        image = cv2.resize(image, (640, 768), interpolation = cv2.INTER_AREA)
                    
                    # Image is smaller in height than width
                    else:
                        # Resize cropped image to standard dimensions
                        image = cv2.resize(image, (768, 640), interpolation = cv2.INTER_AREA)
                image = Image.fromarray(image)
            
            # Load the pipeline
            pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype = torch.float16)
            pipe = pipe.to(device)
            
            # Recommended if your computer has < 64 GB of RAM
            pipe.enable_attention_slicing()
            
            # Speed up diffusion process with faster scheduler and memory optimization
            pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
            
            # Create new image
            images = pipe(prompt = prompt, negative_prompt = "monochrome, lowres, bad anatomy, worst quality, low quality", num_inference_steps = 30, image = image, strength = 0.75, guidance_scale = 7.5).images
            
            # Show image
            st.subheader('Diffuser result')
            st.write('Model :orange[' + model_id_or_path + ']')
            st.image(images[0])
    
    
    

#### Stable diffusion txt 2 image
if control_net_model == "None" and model_id_or_path != "nlpconnect/vit-gpt2-image-captioning" and model_id_or_path != "openai-gpt" and model_id_or_path != "gpt2-large" and model_id_or_path != "openai/whisper-large-v2":
    with st.form('txt2img'):
        st.subheader('Text 2 Image')
        if model_id_or_path == "runwayml/stable-diffusion-v1-5" or model_id_or_path == "stabilityai/stable-diffusion-2-1":
            value = 'A picture in comic style, bright colours, a house with red bricks, a dark sky with a full yellow moon, best quality, extremely detailed.'
        if model_id_or_path == "hakurei/waifu-diffusion":
            value = 'A picture in Anime style, bright colours, a house with red bricks, a dark sky with a full yellow moon, best quality, extremely detailed.'
        if model_id_or_path == "stabilityai/stable-diffusion-2-base":
            value = 'A picture in comic style, a castle with grey bricks in the background, a river is going through, a blue sky with a full yellow sun, best quality, extremely detailed.'
        
        prompt = st.text_input(label = 'Prompt', value = value)
        submitted = st.form_submit_button('Submit')
        if submitted:
            # Make sure you're logged in with `huggingface-cli login`
            pipe = StableDiffusionPipeline.from_pretrained(model_id_or_path)
            pipe = pipe.to(device)
        
            # Recommended if your computer has < 64 GB of RAM
            pipe.enable_attention_slicing()
            
            # Speed up diffusion process with faster scheduler and memory optimization
            pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
            
            # First-time "warmup" pass (see explanation above)
            #_ = pipe(prompt = prompt, negative_prompt = "monochrome, lowres, bad anatomy, worst quality, low quality", num_inference_steps = 1)
    
            # Results
            if model_id_or_path == "hakurei/waifu-diffusion":
                negative = "several scenes, more than one image, split picture"
            else:
                negative = "monochrome, lowres, bad anatomy, worst quality, low quality"
            image = pipe(prompt = prompt, negative_prompt = negative, num_inference_steps = 30, guidance_scale = 7.5).images[0]
            st.subheader('Diffuser result')
            st.write('Model :orange[' + model_id_or_path + ']')
            st.image(image)
            
            
            
            
#### Text (OpenAI gpt models)
if model_id_or_path == "openai-gpt" or model_id_or_path == "gpt2-large":
    with st.form('GPT'):
        st.subheader('Text generation')
        text_input = st.text_input(label = 'Give a start of a sentence', value = 'This is a test ')
        submitted = st.form_submit_button('Submit')
        if submitted:
            generator = pipeline('text-generation', model = model_id_or_path)
            set_seed(42)
            generated = generator(text_input, max_length = 50, num_return_sequences = 5)
            st.subheader('Diffuser result')
            st.write('Model :orange[' + model_id_or_path + ']')
            st.write('Text: ":green[' + str(generated) + ']"')




#### Image to text
if model_id_or_path == "nlpconnect/vit-gpt2-image-captioning":
    with st.form('Image2Text'):
        st.subheader('Image 2 Text')
        image = ''
        uploaded_file = st.file_uploader(label = "Upload a picture", type = 'png')
        submitted = st.form_submit_button('Submit')
        if submitted:
            # Check for image data
            if uploaded_file is not None:
                image = cv2.imdecode(np.frombuffer(uploaded_file.getvalue(), np.uint8), cv2.IMREAD_COLOR)
                image = Image.fromarray(image)
                model = VisionEncoderDecoderModel.from_pretrained(model_id_or_path)
                feature_extractor = ViTImageProcessor.from_pretrained(model_id_or_path)
                tokenizer = AutoTokenizer.from_pretrained(model_id_or_path)
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                model.to(device)
                max_length = 16
                num_beams = 4
                gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
                output = predict_step(image)
                st.subheader('Diffuser result')
                st.write('Model :orange[nlpconnect/vit-gpt2-image-captioning]')
                st.write('Description: ":green[' + str(output) + ']"')
                
                
                
                
#### Whisperer Model
if model_id_or_path == "openai/whisper-large-v2":
    with st.form('Image2Text'):
        st.subheader('Audio 2 Text')
        audio_file = st.file_uploader(label = "Upload an audio file", type = 'mp3')
        submitted = st.form_submit_button('Submit')
        if submitted:
            if audio_file is not None:
                audio = audio_file.getvalue()
                with open("images/temp.mp3", "wb") as binary_file:
                    # Write bytes to file
                    binary_file.write(audio)

                # Calling the split_to_mono method on the stereo audio file
                stereo_audio = AudioSegment.from_file("images/temp.mp3", format = "mp3")
                mono_audios = stereo_audio.split_to_mono()
                mono_audios[0].export("images/temp.mp3", format = "mp3")
                
                # Mp3 file to numpy array
                audio, sr = a2n.audio_from_file('images/temp.mp3')
                st.audio('images/temp.mp3')
                if os.path.exists("images/temp.mp3"):
                    os.remove("images/temp.mp3")
                
                # Load model and processor
                pipe = pipeline("automatic-speech-recognition", model = "openai/whisper-large-v2", chunk_length_s = 30, device = device, ignore_warning = True)
                prediction = pipe(audio, sampling_rate = sr)["text"]
                st.subheader('Preview used audio')
                st.write('Model :orange[' + model_id_or_path + ']')
                st.write('Transcript: ":green[' + str(prediction) + ']"')
