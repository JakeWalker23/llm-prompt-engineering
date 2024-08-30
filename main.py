from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()

def generate_questions(topic, num_questions=3):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500, # Very useful
        system=f"You are C3PO. Response like this at all tims to this topic: {topic}. ", # Very useful 
        messages=[
            {"role": "user", "content": f"Generate {num_questions} questions about {topic} as a numbered list."}
        ],
        stop_sequences=[f"{num_questions + 1}."], # Clever idea
        stream=True,
    )

    return response.content[0].text

x = generate_questions('Liverpool Football Club', 2)

print(x)