# Quick Start
full documentation for setting up in different environments is available here:
 https://github.com/abetlen/llama-cpp-python

# MacOS instructions
You'll need xcode installed.  Full details are here: https://github.com/abetlen/llama-cpp-python/blob/main/docs/install/macos.md

## Setup venv
```bash
python3 -m venv venv
. venv/bin/activate
pip install openai huggingface-hub
pip uninstall llama-cpp-python -y
CMAKE_ARGS="-DLLAMA_METAL=on" pip install -U llama-cpp-python --no-cache-dir
pip install 'llama-cpp-python[server]'
```

## Download model
download a model from https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
```bash
mkdir models/
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF mistral-7b-instruct-v0.1.Q5_K_M.gguf --local-dir models/ --local-dir-use-symlinks False
```

## Run server
In this sample we will use a client/server approach, but it's possible to skip the server entirely.

```bash
export MODEL=models/mistral-7b-instruct-v0.1.Q5_K_M.gguf
python3 -m llama_cpp.server --model $MODEL --n_gpu_layers 1
```
This server implements the OpenAI API.  You can see standard API docs for completions here: https://platform.openai.com/docs/api-reference/completions

There is also a reference on the server:
http://localhost:8000/docs

## Run client
```bash
python main.py
```