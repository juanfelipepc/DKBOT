import requests

from botconfig import telegram_token

API_URL = 'https://api.telegram.org'
ROOT_URL = f'{API_URL}/bot{telegram_token}/'


def get_updates():
    UPDATES_URL = ROOT_URL + 'getUpdates'
    update_params = {'offset': '-1', 'limit': '1'}
        
    try:
        response = requests.get(UPDATES_URL, params=update_params)
        data = response.json()
    except:
        raise ValueError("Failed to get updates")
    
    return data


def send_message(group_id, message):
    SEND_URL = ROOT_URL + 'sendMessage'
    msg_params = {'chat_id': group_id, 'text': message}

    try:
        response = requests.post(SEND_URL, params=msg_params)
    except:
        raise ValueError("Failed to send message")
