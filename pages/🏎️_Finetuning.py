##### `🏎️_Finetuning.py`
##### Model Finetuning
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st

# Set up the Streamlit app layout
st.set_page_config(page_title="Model Finetuning", page_icon="🏎️")
st.title("🏎️ Finetuning a LLM")
st.markdown("""
Fine-Tuning Llama 3 and Using It Locally: A Step-by-Step Guide
We'll fine-tune Llama 3 on a dataset of patient-doctor conversations, creating a model tailored for medical dialogue. 
After merging, converting, and quantizing the model, it will be ready for private local use via the Jan application. View the article
[article for this app](https://www.datacamp.com/tutorial/llama3-fine-tuning-locally?dc_referrer=https%3A%2F%2Fwww.bing.com%2F).
""")
