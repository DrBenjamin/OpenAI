# OpenAI

[![GitHub][github_badge]][github_link]

Playground for using OpenAI ChatGPT and Hugging Face state-of-the-art diffusion models for image, text and audio generation in PyTorch.

## Local Installation to use the Hugging Face models

Download the [Package](https://github.com/DrBenjamin/OpenAI/archive/refs/tags/v1.0.zip) and install the needed libraries with

```bash
python -m pip install --upgrade -r requirements.txt
```

Create Python Environment

```bash
conda create --name myenv python=3.10
conda activate myenv
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

## Llama.cpp

Get the sources, build and run the Llama3 model with the following commands:
```bash
 git clone https://github.com/ggerganov/llama.cpp.git
 cd llama.cpp
 make
 ./llama-server -m ~/.cache/lm-studio/models/DrBenjamin/llama-3-8b-chat-doctor/llama-3-8b-chat-doctor-Q4_K_M.gguf --port 1234 -c 2048
```

## Fine-tuning the Llama3 model

Example of fine-tuning the Llama3 model on a medical conversation dataset.

[Link to Kaggle](https://www.kaggle.com/work/collections/14192615)
[Link to Wandb](https://wandb.ai/seriousbenentertainment/Fine-tune%20Llama%203%208B%20on%20Medical%20Dataset)
[Link to Huggingface](https://huggingface.co/DrBenjamin/llama-3-8b-chat-doctor/tree/main)

## Streamlit Cloud Demo

[![Open in Streamlit][share_badge]][share_link]

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/DrBenjamin/OpenAI

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://ai-playground.streamlit.app/

## Snowflake Native App Framework

[Python modules in Snowflake](https://repo.anaconda.com/pkgs/snowflake/)

```bash
brew tap snowflakedb/snowflake-cli
brew install snowflake-cli
python -m pip install --upgrade --force-reinstall snowflake-cli-labs
```

### Snowflake Data Warehouse

https://eur02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fj06yswzb.r.eu-west-1.awstrack.me%2FL0%2Fhttps%3A%252F%252Fffcjeqr-pk52190.snowflakecomputing.com%2F1%2F01020191129e984f-6e5b7a42-b1ec-4d7b-8cc5-11a8d2d8da2e-000000%2FiDdZFp2mYbYtF8GgC0zZik4BShc%3D385&data=05%7C02%7C%7C2241ef25f06d4159b50b08dcb2dd511f%7C2e9f06b016694589878910a06934dc61%7C0%7C0%7C638581910815793088%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=Cvqw%2B276kI9yznl3NXTozxRc%2BI6NjIvdOqefiFuWcdY%3D&reserved=0

## Misc

Miscellaneous files and scripts for the project.

```bash
git repack -a -d -f --depth=250 --window=250
git gc --aggressive --prune
```
