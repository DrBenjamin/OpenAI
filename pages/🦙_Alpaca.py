##### `🦙_Alpaca.py`
##### Alpaca Model
##### https://github.com/ggerganov/llama.cpp (llama.cpp)
##### https://github.com/cocktailpeanut/dalai (download models)
##### https://github.com/shaunabanana/llama.py (llama wrapper)
##### https://github.com/abetlen/llama-cpp-python (python package for bindings)
##### Please reach out to drdrbenjamin@icloud.com for any questions
#### Loading needed Python libraries
import streamlit as st
import subprocess
import sys
# sys.path.insert(1, "pages/modules")
# from llama_wrapper import llama_wrapper
from llama_cpp import Llama

#### Streamlit initial setup
st.set_page_config(
    page_title = "🦙 Alpaca",
    page_icon = "images/Logo.png",
    layout = "centered",
    initial_sidebar_state = "expanded"
)

#### Main programs
### Python Wrapper / Bindings
with st.form('Alpaca'):
    st.header('Alpaca LLM')
    st.write(
        'LLaMA is a collection of foundation language models ranging from 7B to 65B parameters, trained on trillions of tokens to show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. All models aree publically released to the research community.')
    instructions = ['https://github.com/ggerganov/llama.cpp (llama.cpp)',
                    'https://github.com/cocktailpeanut/dalai (download models)',
                    'https://github.com/shaunabanana/llama.py (llama wrapper)',
                    'https://github.com/abetlen/llama-cpp-python (python package for bindings)']
    st.write(':orange[Needs to be run locally:] ' + instructions[0] + ' ' + instructions[1] + ' ' + instructions[2] + ' ' + instructions[3])
    mode = st.radio('Mode', ('Wrapper (faster)', 'Bindings (slower)'), index = 1, disabled = True)
    st.subheader('Question')
    input_text = st.text_input('Ask a question')
    input_text = 'I am `Ben`, an Artifcial AI and you I am living in a blue box, the `BenBox`. My purpose as AI called `Ben` is to support the crew of the spaceship `Pulp`. The crew consists of me `Ben`, `Emmi` the female mechanic, `Sertan` who is doing computer stuff and the 2 robots `SAM` and `SEB`. At the moment, I, `Ben`, have landed with the Pulp and the crew on the Earth. The ship landed in Cologne, Germany, next to the University. Me, `Ben` and `Sertan will go on our next mission, to explore the golden chamber in church `St. Ursula`. Me, `Ben`, will answer all your questions in a humorous, sarcastic and very brief way. `Ben` please answer to this question or comment: """' + input_text + '"""'
    submitted = st.form_submit_button('Submit')
    if submitted:
        try:
            if mode == 'Wrapper (faster)':
                output = llama_wrapper(prompt = input_text, stream = False, temperature = 0.5)
                output = output[len(input_text):]
                output = output.replace('Answer', '')
                output = output.replace('by Ben: ', '')
                output = output.replace('by Ben : ', '')
                output = output.replace('Answer: ', '')
                output = output.strip()
            elif mode == 'Bindings (slower)':
                llm = Llama(model_path = "models/7B/ggml-model-q4_0.bin", verbose = True)
                output = llm("Q: " + input_text + "A: ", max_tokens = 128, stop = ["Q:", "\n"], echo = True)
                output = output['choices'][0]['text']
                output = output.replace("Q: " + input_text + "A: ", '')
            st.subheader('Answer')
            st.write('Answer: :green[' + output + ']')
        except Exception as e:
            st.error(body = str(e) + ' Please run locally!', icon = "🚨")
