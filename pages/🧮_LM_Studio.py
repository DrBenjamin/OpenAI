import streamlit as st
from openai import OpenAI
# Pointing to the local server
client = OpenAI(base_url="http://192.168.178.24:1234/v1", api_key="lm-studio")

prompt = ""
prompt = st.text_input("Prompt")
if prompt != "":
  completion = client.chat.completions.create(
    model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
    messages=[
      {"role": "system", "content": "You are a friendly chat bot."},
      {"role": "user", "content": prompt}
    ],
    temperature=0.7,
  )

  st.write(completion.choices[0].message.content)