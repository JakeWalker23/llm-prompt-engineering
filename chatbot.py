from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

conversation_history = []


while True:
    user_input = input('User: ')

    conversation_history.append({"role" : "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        messages=conversation_history,
        max_tokens=500,
    )

    print(response.content[0].text)
    
    conversation_history.append({"role" : "assistant", "content": response.content[0].text })
