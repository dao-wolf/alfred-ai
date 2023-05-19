import os
import openai

# Replace with your actual OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
max_tokens = 256
temperature = 0.5


def chatCompletion(userMessage):
    # For chat-based interactions
    prompt = [{"role": "user", "content": userMessage}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
