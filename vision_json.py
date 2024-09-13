from helpers.image_source import create_image_message

from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

messages = [
    {
        "role": "user", 
        "content": 
        [ 
            {"type": "text", "text": "Image 1:"},                                           # When working with lesser capable models, labelling images can be very helpful.
            create_image_message('./Image/flip.png'),
            {"type": "text", "text": "Image 2:"},
            create_image_message('./Image/shot.png'),
            {"type": "text", "text": "You have perfect vision and pay great attention to detail in images. How many people flags are in this picture? Some of the flags may be partially obscured or cut off in the image or may be visible. Please count flags even if you can only see a single aspect. Before providing the answer in <answer> tags, think step by step in <thinking> tags and analyze every part of the image."}
        ]
    },
]

response = client.messages.create(
    model="claude-3-haiku-20240307", # Different models have different capabilities.
    max_tokens=2048,
    messages=messages,
)

print(response.content[0].text)