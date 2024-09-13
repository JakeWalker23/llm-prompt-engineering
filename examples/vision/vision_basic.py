from anthropic import Anthropic
from dotenv import load_dotenv
import base64
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()


with open('./Image/flip.png', "rb") as image_file:
    binary_data = image_file.read()

    base_64_encoded_data = base64.b64encode(binary_data)

    base64_string = base_64_encoded_data.decode('utf-8')

messages = [
    {
        "role": "user", 
        "content": [
            {"type" : "image", "source" : {
                "type" : "base64",
                "media_type": "image/png",
                "data" : base64_string
            }},
            {
                "type" : "text",
                "text" : "Do you know what move she is performing?"
            }
        ]
    },
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages,
)

print(response.content[0].text)