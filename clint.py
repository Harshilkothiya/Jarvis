import os
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a Virtual assistant named jarvis skilled in general tasks like alexa and google cloud "
        },
        {
            "role": "user",
            "content": "what is the programing",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)