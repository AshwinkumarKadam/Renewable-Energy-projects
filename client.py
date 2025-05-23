


client = OpenAI(

    api_key="sk-1234qrstuvwxabcd1234qrstuvwxabcd1234qrst",
)

completion = client.chat.completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding" }
    ]

)