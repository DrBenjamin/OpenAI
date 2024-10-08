##### `💁‍ Open_Assistant.py`
##### Chat Llm Streaming
##### https://huggingface.co/spaces/olivierdehaene/chat-llm-streaming/blob/main/README.md
##### https://open-assistant.io/dashboard
##### https://github.com/LAION-AI/Open-Assistant
##### Please reach out to drdrbenjamin@icloud.com for any questions
#### Loading needed Python libraries
import streamlit as st
import os
from text_generation import Client, InferenceAPIClient
from text_generation import InferenceAPIClient




#### Streamlit initial setup
st.set_page_config(
  page_title = "💁 Open Assistant LLM",
  page_icon = "images/OpenAssistant.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)




#### Main program
st.header('💁‍ Open Assistant LLM')
st.write('Conversational AI for everyone.')
st.write('In the same way that Stable Diffusion helped the world make art and images in new ways, this helps to improve the world by providing amazing conversational AI.')
st.write('This is the first iteration English supervised-fine-tuning (SFT) model of the Open-Assistant project. It is based on a Pythia 12B that was fine-tuned on ~22k human demonstrations of assistant conversations collected through the https://open-assistant.io/ human feedback web app before March 7, 2023.')
st.write(':orange[Needs to be run on Hugging Face to access the OpenAssistant model (Run it here https://huggingface.co/spaces/DrBenjamin/AI_Demo or in the Streamlit Cloud https://ai-playground.streamlit.app).]')
with st.form('OpenAssistant'):
  client = InferenceAPIClient("OpenAssistant/oasst-sft-1-pythia-12b")
  st.subheader('Question')
  input_text = st.text_input('Ask a question')
  input_text = '<|prompter|>' + input_text + '<|endoftext|><|assistant|>'
  submitted = st.form_submit_button('Submit')
  if submitted:
    text = client.generate(input_text).generated_text
    st.subheader('Answer')
    st.write('Answer: :green[' + str(text) + ']')


# Token Streaming
#text = ""
#for response in client.generate_stream("<|prompter|>Why is the sky blue?<|endoftext|><|assistant|>"):
#   if not response.token.special:
#       print(response.token.text)
#       text += response.token.text
#st.write(text)

#
# openchat_preprompt = (
#     "\n<human>: Hi!\n<bot>: My name is Bot, model version is 0.15, part of an open-source kit for "
#     "fine-tuning new bots! I was created by Together, LAION, and Ontocord.ai and the open-source "
#     "community. I am not human, not evil and not alive, and thus have no thoughts and feelings, "
#     "but I am programmed to be helpful, polite, honest, and friendly.\n"
# )
#
#
# def get_client(model: str):
#     if model == "togethercomputer/GPT-NeoXT-Chat-Base-20B":
#         return Client(os.getenv("OPENCHAT_API_URL"))
#     return InferenceAPIClient(model, token = os.getenv("HF_TOKEN", None))
#
#
# def get_usernames(model: str):
#     """
#     Returns:
#         (str, str, str, str): pre-prompt, username, bot name, separator
#     """
#     if model == "OpenAssistant/oasst-sft-1-pythia-12b":
#         return "", "<|prompter|>", "<|assistant|>", "<|endoftext|>"
#     if model == "togethercomputer/GPT-NeoXT-Chat-Base-20B":
#         return openchat_preprompt, "<human>: ", "<bot>: ", "\n"
#     return "", "User: ", "Assistant: ", "\n"
#
#
# def predict(
#         model: str,
#         inputs: str,
#         typical_p: float,
#         top_p: float,
#         temperature: float,
#         top_k: int,
#         repetition_penalty: float,
#         watermark: bool,
#         chatbot,
#         history,
# ):
#     client = get_client(model)
#     preprompt, user_name, assistant_name, sep = get_usernames(model)
#
#     history.append(inputs)
#
#     past = []
#     for data in chatbot:
#         user_data, model_data = data
#
#         if not user_data.startswith(user_name):
#             user_data = user_name + user_data
#         if not model_data.startswith(sep + assistant_name):
#             model_data = sep + assistant_name + model_data
#
#         past.append(user_data + model_data.rstrip() + sep)
#
#     if not inputs.startswith(user_name):
#         inputs = user_name + inputs
#
#     total_inputs = preprompt + "".join(past) + inputs + sep + assistant_name.rstrip()
#
#     partial_words = ""
#
#     if model == "OpenAssistant/oasst-sft-1-pythia-12b":
#         iterator = client.generate_stream(
#             total_inputs,
#             typical_p = typical_p,
#             truncate = 1000,
#             watermark = watermark,
#             max_new_tokens = 500,
#         )
#     else:
#         iterator = client.generate_stream(
#             total_inputs,
#             top_p = top_p if top_p < 1.0 else None,
#             top_k = top_k,
#             truncate = 1000,
#             repetition_penalty = repetition_penalty,
#             watermark = watermark,
#             temperature = temperature,
#             max_new_tokens = 500,
#             stop_sequences = [user_name.rstrip(), assistant_name.rstrip()],
#         )
#
#     for i, response in enumerate(iterator):
#         if response.token.special:
#             continue
#
#         partial_words = partial_words + response.token.text
#         if partial_words.endswith(user_name.rstrip()):
#             partial_words = partial_words.rstrip(user_name.rstrip())
#         if partial_words.endswith(assistant_name.rstrip()):
#             partial_words = partial_words.rstrip(assistant_name.rstrip())
#
#         if i == 0:
#             history.append(" " + partial_words)
#         elif response.token.text not in user_name:
#             history[-1] = partial_words
#
#         chat = [
#             (history[i].strip(), history[i + 1].strip())
#             for i in range(0, len(history) - 1, 2)
#         ]
#         yield chat, history
#
#
# def reset_textbox():
#     return gr.update(value = "")
#
#
# def radio_on_change(
#         value: str,
#         disclaimer,
#         typical_p,
#         top_p,
#         top_k,
#         temperature,
#         repetition_penalty,
#         watermark,
# ):
#     if value == "OpenAssistant/oasst-sft-1-pythia-12b":
#         typical_p = typical_p.update(value = 0.2, visible = True)
#         top_p = top_p.update(visible = False)
#         top_k = top_k.update(visible = False)
#         temperature = temperature.update(visible = False)
#         disclaimer = disclaimer.update(visible = False)
#         repetition_penalty = repetition_penalty.update(visible = False)
#         watermark = watermark.update(False)
#     elif value == "togethercomputer/GPT-NeoXT-Chat-Base-20B":
#         typical_p = typical_p.update(visible = False)
#         top_p = top_p.update(value = 0.25, visible = True)
#         top_k = top_k.update(value = 50, visible = True)
#         temperature = temperature.update(value = 0.6, visible = True)
#         repetition_penalty = repetition_penalty.update(value = 1.01, visible = True)
#         watermark = watermark.update(False)
#         disclaimer = disclaimer.update(visible = True)
#     else:
#         typical_p = typical_p.update(visible = False)
#         top_p = top_p.update(value = 0.95, visible = True)
#         top_k = top_k.update(value = 4, visible = True)
#         temperature = temperature.update(value = 0.5, visible = True)
#         repetition_penalty = repetition_penalty.update(value = 1.03, visible = True)
#         watermark = watermark.update(True)
#         disclaimer = disclaimer.update(visible = False)
#     return (
#         disclaimer,
#         typical_p,
#         top_p,
#         top_k,
#         temperature,
#         repetition_penalty,
#         watermark,
#     )
#
#
# title = """<h1 align="center">🔥Large Language Model API 🚀Streaming🚀</h1>"""
# description = """Language models can be conditioned to act like dialogue agents through a conversational prompt that typically takes the form:
# ```
# User: <utterance>
# Assistant: <utterance>
# User: <utterance>
# Assistant: <utterance>
# ...
# ```
# In this app, you can explore the outputs of multiple LLMs when prompted in this way.
# """
#
# openchat_disclaimer = """
# <div align="center">Checkout the official <a href=https://huggingface.co/spaces/togethercomputer/OpenChatKit>OpenChatKit feedback app</a> for the full experience.</div>
# """
#
# with gr.Blocks(
#         css = """#col_container {margin-left: auto; margin-right: auto;}
#                 #chatbot {height: 520px; overflow: auto;}"""
# ) as demo:
#     gr.HTML(title)
#     with gr.Column(elem_id = "col_container"):
#         model = gr.Radio(
#             value = "OpenAssistant/oasst-sft-1-pythia-12b",
#             choices = [
#                 "OpenAssistant/oasst-sft-1-pythia-12b",
#                 # "togethercomputer/GPT-NeoXT-Chat-Base-20B",
#                 "google/flan-t5-xxl",
#                 "google/flan-ul2",
#                 "bigscience/bloom",
#                 "bigscience/bloomz",
#                 "EleutherAI/gpt-neox-20b",
#             ],
#             label = "Model",
#             interactive = True,
#         )
#
#         chatbot = gr.Chatbot(elem_id = "chatbot")
#         inputs = gr.Textbox(
#             placeholder = "Hi there!", label = "Type an input and press Enter"
#         )
#         disclaimer = gr.Markdown(openchat_disclaimer, visible = False)
#         state = gr.State([])
#         b1 = gr.Button()
#
#         with gr.Accordion("Parameters", open = False):
#             typical_p = gr.Slider(
#                 minimum = -0,
#                 maximum = 1.0,
#                 value = 0.2,
#                 step = 0.05,
#                 interactive = True,
#                 label = "Typical P mass",
#             )
#             top_p = gr.Slider(
#                 minimum = -0,
#                 maximum = 1.0,
#                 value = 0.25,
#                 step = 0.05,
#                 interactive = True,
#                 label = "Top-p (nucleus sampling)",
#                 visible = False,
#             )
#             temperature = gr.Slider(
#                 minimum = -0,
#                 maximum = 5.0,
#                 value = 0.6,
#                 step = 0.1,
#                 interactive = True,
#                 label = "Temperature",
#                 visible = False,
#             )
#             top_k = gr.Slider(
#                 minimum = 1,
#                 maximum = 50,
#                 value = 50,
#                 step = 1,
#                 interactive = True,
#                 label = "Top-k",
#                 visible = False,
#             )
#             repetition_penalty = gr.Slider(
#                 minimum = 0.1,
#                 maximum = 3.0,
#                 value = 1.03,
#                 step = 0.01,
#                 interactive = True,
#                 label = "Repetition Penalty",
#                 visible = False,
#             )
#             watermark = gr.Checkbox(value = False, label = "Text watermarking")
#
#     model.change(
#         lambda value: radio_on_change(
#             value,
#             disclaimer,
#             typical_p,
#             top_p,
#             top_k,
#             temperature,
#             repetition_penalty,
#             watermark,
#         ),
#         inputs = model,
#         outputs = [
#             disclaimer,
#             typical_p,
#             top_p,
#             top_k,
#             temperature,
#             repetition_penalty,
#             watermark,
#         ],
#     )
#
#     inputs.submit(
#         predict,
#         [
#             model,
#             inputs,
#             typical_p,
#             top_p,
#             temperature,
#             top_k,
#             repetition_penalty,
#             watermark,
#             chatbot,
#             state,
#         ],
#         [chatbot, state],
#     )
#     b1.click(
#         predict,
#         [
#             model,
#             inputs,
#             typical_p,
#             top_p,
#             temperature,
#             top_k,
#             repetition_penalty,
#             watermark,
#             chatbot,
#             state,
#         ],
#         [chatbot, state],
#     )
#     b1.click(reset_textbox, [], [inputs])
#     inputs.submit(reset_textbox, [], [inputs])
#
#     gr.Markdown(description)
#     demo.queue(concurrency_count = 16).launch(debug = True)
