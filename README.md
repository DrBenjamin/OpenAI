# OpenAI

[![GitHub][github_badge]][github_link]

Playground for using OpenAI ChatGPT and Hugging Face state-of-the-art diffusion models for image, text and audio generation in PyTorch.

## Local Installation to use the Hugging Face models

Download the [Package](https://github.com/DrBenjamin/OpenAI/archive/refs/tags/v1.0.zip) and install the needed libraries with

```bash
python -m pip install -r requirements.txt
```

Run the software with

```bash
python -m streamlit run 🤖_OpenAI.py
```

Click on `Hugging Face` in the left sidebar and choose a model from the selectbox. The model will be automatically downloaded (stored in `User/.cache` folder). Create the file `.streamlit/secrets.toml` with this content:

```toml
[openai]
key = "openai-api-key"
image = "images/BenBox_small.png"

[hugging_face]
key = "hugging-face-key"
```

## Get llama.cpp

```bash
 git clone https://github.com/ggerganov/llama.cpp.git
```

## Fine-tuning the Llama3 model

[Link to Kaggle](https://www.kaggle.com/work/collections/14192615)

## Streamlit Cloud Demo

[![Open in Streamlit][share_badge]][share_link]

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/DrBenjamin/OpenAI

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://ai-playground.streamlit.app/



