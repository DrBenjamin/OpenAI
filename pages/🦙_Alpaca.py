##### `🦙_Alpaca.py`
##### Alpaca Model
##### https://medium.com/@avra42/how-to-build-a-chatbot-with-chatgpt-api-and-a-conversational-memory-in-python-8d856cda4542
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
from llamacpypy import Llama
import subprocess


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



#text = []
#for token in llama(prompt = 'What is your purpose?', repeat_penalty = 1.05, skip_prompt = False, interactive = False):
#    print(token, end = '', flush = True)
#    text.append(token)
#st.subheader('Debug')
#st.experimental_show(text[0])
#st.experimental_show(text[1])
#st.subheader('Answer')
#st.write(''.join(text))


llama = Llama(model_name = 'models/7B/ggml-model-q4_0.bin', warm_start = True)
llama.load_model()
var = llama.generate("This is the weather report, we are reporting a clown fiesta happening at backer street. The clowns ")
st.write(var)
        