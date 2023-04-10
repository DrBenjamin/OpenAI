##### `🦙_Alpaca.py`
##### Alpaca Model
##### https://github.com/shaunabanana/llama.py
##### https://github.com/seemanne/llamacpypy
##### https://github.com/thomasantony/llamacpp-python
##### https://github.com/abetlen/llama-cpp-python
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
import subprocess
import sys
sys.path.insert(1, "pages/modules")
from llama_wrapper import llama_wrapper
from llama_cpp import Llama




#### Streamlit initial setup
st.set_page_config(
  page_title = "🦙 Alpaca",
  page_icon = "images/Logo.png",
  layout = "centered",
  initial_sidebar_state = "expanded"
)



#### Main programs
### Llama cpp
#llm = Llama(model_path = "models/7B/ggml-model-q4_0.bin")
#output = llm("Q: Name the planets in the solar system? A: ", max_tokens = 32, stop = ["Q:", "\n"], echo = True)
#st.write(output)



### Python Wrapper
with st.form('Alpaca'):
  st.header('Alpaca LLM')
  st.write('LLaMA is a collection of foundation language models ranging from 7B to 65B parameters, trained on trillions of tokens to show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. All models aree publically released to the research community.')
  st.write(':orange[Needs to be run locally (Follow the instructions on https://github.com/shaunabanana/llama.py).]')
  mode = st.radio('Mode', ('Wrapper (faster)', 'Python (slower)'))
  st.subheader('Question')
  input_text = st.text_input('Ask a question')
  input_text = 'I am `Ben`, an Artifcial AI and you I am living in a blue box, the `BenBox`. My purpose as AI called `Ben` is to support the crew of the spaceship `Pulp`. The crew consists of me `Ben`, `Emmi` the female mechanic, `Sertan` who is doing computer stuff and the 2 robots `SAM` and `SEB`. At the moment, I, `Ben`, have landed with the Pulp and the crew on the Earth. The ship landed in Cologne, Germany, next to the University. Me, `Ben` and `Sertan will go on our next mission, to explore the golden chamber in church `St. Ursula`. Me, `Ben`, will answer all your questions in a humorous, sarcastic and very brief way. `Ben` please answer to this question or comment: """' + input_text + '"""'
  #input_text = 'Extract keywords in this text: """' + input_text + '"""'
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
      elif mode == 'Python (slower)':
        llm = Llama(model_path = "models/7B/ggml-model-q4_0.bin")
        output = llm("Q: " + input_text + "A: ", max_tokens = 128, stop = ["Q:", "\n"], echo = True)
        output = output['choices'][0]['text']
        output = output.replace("Q: " + input_text + "A: ", '')
      st.subheader('Answer')
      st.write('Answer: :green[' + output + ']')
    except Exception as e:
      st.error(body = str(e) + ' Please run locally!', icon = "🚨")
  


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
#params = llamacpp.gpt_params('./models/7B/ggml-model-q4_0.bin',  # model,
#    512,  # ctx_size
#    100,  # n_predict
#    40,  # top_k
#    0.95,  # top_p
#    0.85,  # temp
#    1.30,  # repeat_penalty
#    -1,  # seed
#    8,  # threads
#    64,  # repeat_last_n
#    8,  # batch_size
#)
#model = llamacpp.PyLLAMA(params)
#model.add_bos()     # Adds "beginning of string" token
#model.update_input("A llama is a")
#model.print_startup_stats()
#model.prepare_context()

#model.ingest_all_pending_input(True)
#while not model.is_finished():
#    text, is_finished = model.infer_text()
#    print(text, end="")

#    if is_finished:
#        break

# Flush stdout
#sys.stdout.flush()
#model.print_end_stats()



### Llama python mapping
# Initialize llama context
# params = llama.llama_context_default_params()
#
# n = 512
#
# params.n_ctx = n
# params.n_parts = -1
# params.seed = 1679473604
# params.f16_kv = False
# params.logits_all = False
# params.vocab_only = False
#
# # Set model path accordingly
# ctx = llama.llama_init_from_file('models/ggml-model-q4.bin', params)
#
# # Tokenize text
# tokens = (llama.llama_token * n)()
# n_tokens = llama.llama_tokenize(ctx, 'Q: What is the capital of France? A: ', tokens, n, True)
# if n_tokens < 0:
#     print('Error: llama_tokenize() returned {}'.format(n_tokens))
#     exit(1)
#
# text = "".join(llama.llama_token_to_str(ctx, t) for t in tokens[:n_tokens])
# print(text)
#
# # Evaluate tokens
# for i in range(3):
#     r = llama.llama_eval(ctx, tokens, n_tokens, 0, 12)
#     if r != 0:
#         print('Error: llama_eval() returned {}'.format(r))
#         exit(1)
#     token = llama.llama_sample_top_p_top_k(ctx, tokens, n_tokens , top_k=40, top_p=0.95, temp=0.8, repeat_penalty=1.1)
#     print(token)
#     tokens[n_tokens] = token
#     n_tokens += 1
#     text = "".join(llama.llama_token_to_str(ctx, t) for t in tokens[:n_tokens])
#     print(text)
#
# # # Print timings
# llama.llama_print_timings(ctx)
#
# # # Free context
# llama.llama_free(ctx)
        