import os
import openai

from secret import apiKey

openai.api_key = apiKey

prompt = "Let me begin by "
model = "text-davinci-002"

completion = openai.Completion.create(engine=model, prompt=prompt, max_tokens = 10)

print(completion)
print(prompt)