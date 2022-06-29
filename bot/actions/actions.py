from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType

import requests
import json
import logging

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def extract_variables():
    try:

        f = open('./actions/variables.json',)
  
        # Reading from file
        json_data = json.loads(f.read())

        url_var = json_data['averageTimeApi']

        if url_var.startswith("#"):
            
            f.close()
            return "https://cc360qua.cofidis.pt:1443/chat/rasa/getAverageTime"

        else:
            f.close()

            return url_var
    
    except Exception as e:
        logger.error(str(e))

        return []

def extract_metadata_from_tracker(tracker):
    try:
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        return user_events[-1]['metadata']

    except Exception as e:
        logging.error(str(e))

        return []

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        print("action_session_start")

        metadata = tracker.get_slot("session_started_metadata")

        username_slot = tracker.get_slot("username")

        username_key='username'

        username = metadata['username']

        if username_key in metadata and not username_slot:

            dispatcher.utter_message(response = "utter_greet", username=username)
            
            return [SlotSet('username', username), SlotSet('roomId', tracker.sender_id), ActionExecuted("action_listen")]

        else:

            return [ ActionExecuted("action_listen")]
      
class Handoff(Action):

    def name(self) -> Text:

        return "action_handoff"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any], 
    ) -> List[Dict[Text, Any]]:

        url_var = extract_variables()

        url = url_var + "/1"

        # url = "https://quacctckt01.cofidis.pt:1443/chat/rasa/getAverageTime/1"

        print("URL: {}".format(url))

        payload={}
        headers = {}

        try:
            # response = requests.request("GET", url, headers=headers, data=payload, verify=False)
            json_data = json_data = {
                "status": 200,
                "message": "OK",
                "success": True,
                "responseObject": {
                    "lastSync": 1655801546039,
                    "averageTimeTimemillis": 28207,
                    "seconds":31,
                    "minutes": 0,
                    "hours": 0
                }
            }

            averageTime = json_data['responseObject']
            averageTime_hours = averageTime["hours"]
            averageTime_minutes = averageTime["minutes"]
            averageTime_seconds = averageTime["seconds"]

            print("AVERAGETIME: {}".format(averageTime))

            logger.error("AVERAGETIME: {}".format(averageTime))

            if averageTime is None:

                dispatcher.utter_message(response="utter_handoff_nok")

            elif averageTime_seconds >= 30:

                dispatcher.utter_message(response="utter_handoff_espera", averageTime_hours=averageTime_hours, averageTime_minutes=averageTime_minutes, averageTime_seconds=averageTime_seconds)

            elif averageTime_seconds <0:

                dispatcher.utter_message(response="utter_handoff_noagent")

            elif averageTime_seconds < 30:

                dispatcher.utter_message(response="utter_handoff_ok")
        
            return []
        
        except Exception as e:

            logger.error(str(e))

            dispatcher.utter_message(response="utter_handoff_nok")

            return []



         