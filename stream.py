from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about liverpool football club",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    stream=True,
)

for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")