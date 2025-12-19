import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message_whats(number: str, message: str):
    url = "https://new.whatsbot.org/api/create-message"

    payload={
    'appkey': 'a4c5ad8c-0589-4fb9-8811-73fed4a2fb20',
    'authkey': '3LbxHkhChr8AKAculpXt1B0LA7xWPdDq6XZ1MzXoVxpx0ySxQ9',
    'to': f'+2{number}',
    'message': message,

    }
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return {"send message"}
