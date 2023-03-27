##### `🦙_Alpaca.py`
##### Alpaca Model
##### https://github.com/seemanne/llamacpypy
##### https://github.com/shaunabanana/llama.py
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
#from llamacpypy import Llama
import llamacpp
from llama_cpp import Llama
import os
import subprocess




#### Streamlit initial setup
st.set_page_config(
  page_title = "🦙 Alpaca",
  page_icon = "images/Logo.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)




#### Functions of the Python Wrapper
def llama_stream(
        prompt = '',
        skip_prompt = True,
        trim_prompt = 0,
        executable = 'pages/llama.cpp/main',
        model = 'models/7B/ggml-model-q4_0.bin',
        threads = 4,
        temperature = 0.7,
        top_k = 40,
        top_p = 0.5,
        repeat_last_n = 256,
        repeat_penalty = 1.17647,
        n = 4096,
        interactive = False,
        reverse_prompt = "User:"
):
    command = [
        executable,
        '-m', model,
        '-t', str(threads),
        '--temp', str(temperature),
        '--top_k', str(top_k),
        '--top_p', str(top_p),
        '--repeat_last_n', str(repeat_last_n),
        '--repeat_penalty', str(repeat_penalty),
        '-n', str(n),
        '-p', prompt
    ]
    if interactive:
        command += ['-i', '-r', reverse_prompt]
    
    process = subprocess.Popen(
        command,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    
    token = b''
    generated = ''
    while True:
        token += process.stdout.read(1)
        if token:  # neither empty string nor None
            try:
                decoded = token.decode('utf-8')
                
                trimmed_prompt = prompt
                if trim_prompt > 0:
                    trimmed_prompt = prompt[:-trim_prompt]
                prompt_finished = generated.startswith(trimmed_prompt)
                reverse_prompt_encountered = generated.endswith(reverse_prompt)
                if not skip_prompt or prompt_finished:
                    yield decoded
                if interactive and prompt_finished and reverse_prompt_encountered:
                    user_input = input()
                    process.stdin.write(user_input.encode('utf-8') + b'\n')
                    process.stdin.flush()
                
                generated += decoded
                token = b''
            except UnicodeDecodeError:
                continue
        elif process.poll() is not None:
            return


def llama(
        prompt = '',
        stream = False,
        skip_prompt = False,
        trim_prompt = 0,
        executable = 'pages/llama.cpp/main',
        model = 'models/7B/ggml-model-q4_0.bin',
        threads = 4,
        temperature = 0.7,
        top_k = 40,
        top_p = 0.5,
        repeat_last_n = 256,
        repeat_penalty = 1.17647,
        n = 4096,
        interactive = False,
        reverse_prompt = "User:"
):
    streamer = llama_stream(
        prompt = prompt,
        skip_prompt = skip_prompt,
        trim_prompt = trim_prompt,
        executable = executable,
        model = model,
        threads = threads,
        temperature = temperature,
        top_k = top_k,
        top_p = top_p,
        repeat_last_n = repeat_last_n,
        repeat_penalty = repeat_penalty,
        n = n,
        interactive = interactive,
        reverse_prompt = reverse_prompt
    )
    if stream:
        return streamer
    else:
        return ''.join(list(streamer))



### Python Wrapper (functions above
#text = []
#for token in llama(prompt = 'What is your purpose?', repeat_penalty = 1.05, skip_prompt = False, interactive = False):
#    print(token, end = '', flush = True)
#    text.append(token)
#st.subheader('Debug')
#st.experimental_show(text[0])
#st.experimental_show(text[1])
#st.subheader('Answer')
#st.write(''.join(text))



### llamacpypy
#llama = Llama(model_name = 'models/7B/ggml-model-q4_0.bin', warm_start = True)
#llama.load_model()
#var = llama.generate("This is the weather report, we are reporting a clown fiesta happening at backer street. The clowns ")
#st.write(var)



### llamacpp
#model_path = "./models/7B/ggml-model-q4_0.bin"
#params = llamacpp.gpt_params(model_path, 4096, 40, 0.1, 0.7, 2.0)
#model = llamacpp.PyLLAMA(model_path, params)
#text = model.predict("Hello, I'm a llama.", 10)
#st.write(text)



### Llama cpp
llm = Llama(model_path="models/7B/ggml-model-q4_0.bin")
output = llm("Q: Name the planets in the solar system? A: ", max_tokens = 32, stop = ["Q:", "\n"], echo = True)
st.write(output)
        