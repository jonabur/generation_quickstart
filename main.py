import openai

openai.api_base = "http://localhost:8000/v1"
openai.api_key = "sk-foo"


def completion(prompt):
    # The standard OpenAI Completion API call options are available.
    return openai.Completion.create(
        model="",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        stop=[],
    )


def main():
    # This is the instruct format for Mistral.  Details here:
    # https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1

    prompt = """<s>[INST] Hello, who are you? [/INST]
I'm Assistant, a friendly AI.  How can I help you?</s>
[INST] Can you tell me the capital of Finland? [/INST]
"""
    response = completion(prompt)
    print(response.choices[0].text)


if __name__ == "__main__":
    main()
