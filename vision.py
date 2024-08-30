from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500, 
    messages=[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "tell me a joke"},
        ]
    }
]
)

print(response.content[0].text)