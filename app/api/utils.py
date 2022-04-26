import requests
import yaml
import os

from pathlib import Path

def get_intents():

    url = "http://rasa:5005/domain/"
    headers = {'Accept': 'application/json'}
    payload = {}

    response = requests.request("GET", url, headers=headers)

    response_data = response.json()

    intents = response_data['intents']

    return intents


def update_nlg(utter_name, utter):

    path = os.getcwd()
    print(path)
    data_path = path + '/data/domain.yml'

    with open(data_path) as file:
        documents = yaml.full_load(file)
        utters = documents['responses']

    if utter_name in utters:
        
        utters[utter_name] = [{'text':utter}]
    
    else:
        message = "A resposta ainda não existe"

        return {"message": message}

    documents['responses'] = utters

    with open(data_path, 'w') as file:
        documents = yaml.dump(documents, file)
    
    return {"message" : "Resposta alterada"}

def create_nlg(utter_name, utter):

    path = os.getcwd()
    print(path)
    data_path = path + '/data/domain.yml'

    with open(data_path) as file:
        documents = yaml.full_load(file)
        utters = documents['responses']
    
    if utter_name in utters:

        return {"message": "O nome da resposta já se encontra em utilização"}

    utters[utter_name] = [{'text':utter}]

    documents['responses'] = utters


    with open(data_path, 'w') as file:
        documents = yaml.dump(documents, file)
    
    return {"message" : "Resposta criada"}

def get_nlg():

    path = os.getcwd()
    print(path)
    data_path = path + '/data/domain.yml'

    with open(data_path) as file:
        documents = yaml.full_load(file)
        responses = documents['responses']
    
    return responses
