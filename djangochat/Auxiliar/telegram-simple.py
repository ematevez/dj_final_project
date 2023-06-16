#Creamos un archivo env.py para guardar nuestras credenciales
# BOT_TOKEN= "992737156:AAHJH8m9uf8RmjWp3Sv8hkFAtN6buoMiS1s"
# BOT_KEY= "-1001964635203"
# NEWS_API_KEY="1e43b6c7fadd4dcea5cdc47a263c5fbc"
#Creamos la intefaz con la API de Noticas.

# bot_token = '992737156:AAHJH8m9uf8RmjWp3Sv8hkFAtN6buoMiS1s'
# bot_chatID = '1252733785'

import requests

TELEGRAM_BOT_TOKEN = "992737156:AAHJH8m9uf8RmjWp3Sv8hkFAtN6buoMiS1s"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

chat_id = "1252733785"
message = "La verdad, ni me sorprende"

params = {"chat_id": chat_id, "parse_mode": "Markdown", "text": message}

requests.get(TELEGRAM_API_URL, params=params)