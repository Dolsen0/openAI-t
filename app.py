import openai
from secret import apiKey

openai.api_key = apiKey

message = input("\nYes?\n")
mood = "friendly" # funny, angry, sarcastic, silly, etc.
prompt = f"generate a {mood} response to someone writing the prompt: {message}"
model = "text-davinci-002"


response = openai.Completion.create(engine=model, prompt=prompt, max_tokens = 40)
generated_text = response["choices"][0]["text"]

# print(response)
print(generated_text)