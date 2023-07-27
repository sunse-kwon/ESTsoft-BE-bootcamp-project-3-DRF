import openai
from django.conf import settings


openai.api_key = settings.APIKEY

def gpt_chat(prompt_with_previous):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt_with_previous,
        max_tokens = 1024,
        temperature = 0.5,
        n=5,
        stop=None
    )
    return response["choices"][0]["text"].strip()

