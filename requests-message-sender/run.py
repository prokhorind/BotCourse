import os

import requests


def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'  # or 'HTML' for different formatting options
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error: {response.status_code}")
        print(response.text)


# Replace with your bot token and chat ID
bot_token = os.environ.get("API_TOKEN")
chat_id = os.environ.get("CHAT_ID")


message = "Hello, this is a message from my bot!"


if __name__ == '__main__':
    # Send message
    send_telegram_message(bot_token, chat_id, message)
