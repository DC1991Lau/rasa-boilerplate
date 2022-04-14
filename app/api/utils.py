import requests

def get_intents():

    url = "http://rasa:5005/domain/"
    headers = {'Accept': 'application/json'}
    payload = {}

    response = requests.request("GET", url, headers=headers)

    response_data = response.json()

    intents = response_data['intents']

    return intents