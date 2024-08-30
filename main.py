from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

our_first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000, 
    messages=[{"role" : "user", "content" : "Hi There! Please tell me a joke that somebody in the north of England would understand."}
    ])

print(our_first_message.content[0].text)
