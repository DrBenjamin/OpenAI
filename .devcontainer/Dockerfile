# app/Dockerfile
FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libmemcached11 \
    libmemcachedutil2 \
    build-essential \
    libmemcached-dev \
    libz-dev \
    libxml2-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    python3-dev \
    espeak \
    pkg-config && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools wheel

WORKDIR /app
COPY . .

RUN python -m pip install --upgrade -r requirements.txt

EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "🤖_OpenAI.py"]
