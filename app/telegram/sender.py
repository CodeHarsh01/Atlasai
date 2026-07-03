import json
from pathlib import Path
import requests

CONFIG_FILE = Path(__file__).resolve().parents[1] / "config" / "telegram.json"


def load_telegram():

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def send_message(message):

    config = load_telegram()

    url = f"https://api.telegram.org/bot{config['bot_token']}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": config["chat_id"],
            "text": message
        },
        timeout=15
    )