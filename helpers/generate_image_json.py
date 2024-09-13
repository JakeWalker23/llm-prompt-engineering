from helpers.image_source import create_image_message
from anthropic import Anthropic

from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

def generate_image_json(image_path):

    slide1_response = """{
        "background": "#F2E0BD",
        "title": "Haiku",
        "body": "Our most powerful model, delivering state-of-the-art performance on highly complex tasks and demonstrating fluency and human-like understanding",
        "image": "The image shows a simple line drawing of a human head in profile view, facing to the right. The head is depicted using thick black lines against a pale yellow background. Inside the outline of the head, there appears to be a white, spoked wheel or starburst pattern, suggesting a visualization of mental activity or thought processes. The overall style is minimalist and symbolic rather than realistic."
    }"""

    messages = [
        {
            "role": "user",
            "content": [
                create_image_message(image_path),
                {"type": "text", "text": "Generate a JSON representation of this slide.  It should include the background color, title, body text, and image description"}
            ],
        },
        {
            "role": "assistant",
            "content": slide1_response
        },
        {
            "role": "user",
            "content": [
                create_image_message(image_path),
                {"type": "text", "text": "Generate a JSON representation of this slide.  It should include the background color, title, body text, and image description"}
            ],
        },
    ]

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2048,
        messages=messages
    )

    return response
