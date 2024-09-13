from helpers.image_source import create_image_message
from anthropic import Anthropic
from dotenv import load_dotenv
import os
import base64
import mimetypes

maths_concepts = [
    "./Image/further-maths/matrices.png",
    "./Image/further-maths/polar-coordinates.png",
    "./Image/further-maths/polynomial.png",
    "./Image/further-maths/vectors.png",
    ]

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

def create_image_message(image_path):
    with open(image_path, "rb") as image_file:

        binary_data = image_file.read()
    
    base64_encoded_data = base64.b64encode(binary_data)
    
    base64_string = base64_encoded_data.decode('utf-8')
    
    mime_type, _ = mimetypes.guess_type(image_path)
    
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }
    
    
    return image_block

def transcribe_single_page(page_url):
    messages = [
    {
        "role": "user",
        "content": [
            create_image_message(page_url),
            {"type": "text", "text": "transcribe the text from this page of mathematical concepts as accurately as possible."}
            ]
        }
    ]

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=5000,
        messages=messages
    )
    return response.content[0].text

def summarize_paper(pages):
    complete_paper_text = ""
    for page in pages:
        transribed_text = transcribe_single_page(page)
        complete_paper_text += transribed_text
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=5000,
        messages=[
            {
                "role": "user",
                "content": f"This is the transcribed contents of a research paper <paper>{complete_paper_text}</paper>.  Please summarize this paper for a non-research audience in at least 3 paragraphs.  Make to sure explain any abbreviations or technical jargon, and use analogies when possible"
            }
        ]
    )

    print(response.content[0].text)

summarize_paper(maths_concepts)
