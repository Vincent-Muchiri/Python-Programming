import requests


CHAT_ID = -5011511352
API_KEY = "5429564331:AAEsvFepPY5nRwDoRBQU-SL6tWtBTTPRBr8"
URL = "https://api.telegram.org/bot5429564331:AAEsvFepPY5nRwDoRBQU-SL6tWtBTTPRBr8/sendMessage"
message = ""
params = {
    "chat_id": CHAT_ID,
    "text": "Testing"
}

response = requests.get(url=URL, params=params)
response.raise_for_status()
print(response.json())