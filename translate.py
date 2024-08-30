from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

client = Anthropic()


def translate( word, language ):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"translate {word} into {language}. Reply only with 1 word."}
        ]
    )

    return response.content[0].text


print(translate('Nutter', 'Australian')) # Wally hahaha 