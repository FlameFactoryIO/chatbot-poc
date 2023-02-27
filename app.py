import os
import openai
from dotenv import load_dotenv

load_dotenv()

# get API key from top-right dropdown on OpenAI website
openai.api_key = os.getenv('OPENAI_API_KEY')

# first let's make it simpler to get answers
def complete(prompt):
    # query text-davinci-003
    res = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    print(res)
    return res['choices'][0]['text'].strip()

query = [
    "si un cliente llama a una companía aerea y pregunta: cuando llega mi ticket. A qué se refiere: a la compra de un billete de avión, a un cambio en un vuelo o un problema con su equipaje?"
]

print(complete(query))
