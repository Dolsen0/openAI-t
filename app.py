import os
import openai

from secret import apiKey

openai.api_key = apiKey

prompt = input("\nwhat would you like to say?\n")
model = "text-davinci-002"


response = openai.Completion.create(engine=model, prompt=prompt, max_tokens = 10)
generated_text = response["choices"][0]["text"]

# print(response)
print(generated_text)