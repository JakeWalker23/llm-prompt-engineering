from anthropic import Anthropic
from anthropic import AsyncAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_key = os.getenv('ANTHROPIC_API_KEY')

# Using Python

client = Anthropic()

stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Can you give me some key details on the flop golf shot",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    stream=True,
)

for event in stream:
    if event.type == "message_start":
        input_tokens = event.message.usage.input_tokens
        print("MESSAGE START EVENT", flush=True)
        print(f"Input tokens used: {input_tokens}", flush=True)
    elif event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")
    elif event.type == "message_delta":
        output_tokens = event.usage.output_tokens
        print("\n========================", flush=True)
        print("MESSAGE DELTA EVENT", flush=True)
        print(f"Output tokens used: {output_tokens}", flush=True)



# Using AsyncAnthropic

# client = AsyncAnthropic()

# async def streaming_with_helpers():
#     async with client.messages.stream(
#         max_tokens=1024,
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Write me a sonnet about orchids"
#             }
#         ],
#         model="claude-3-opus-20240229",
#     ) as stream:
#         async for text in stream.text_stream:
#             print(text, end="", flush=True)
    
#     final_message = await stream.get_final_message()
#     print("\n\nSTREAMING IS DONE.  HERE IS THE FINAL ACCUMULATED MESSAGE: ")
#     print(final_message.to_json())


#     await streaming_with_helpers()