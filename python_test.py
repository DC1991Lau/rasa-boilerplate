import json

response = {
  "version": "3.1",
  "intents": [
    "affirm",
    "bot_challenge",
    "deny",
    "goodbye",
    "greet",
    "mood_great",
    "mood_unhappy"
  ],
  "responses": {
    "utter_greet": [
      {
        "text": "Hey! How are you?"
      }
    ],
    "utter_cheer_up": [
      {
        "text": "Here is something to cheer you up:",
        "image": "https:\/\/i.imgur.com\/nGF1K8f.jpg"
      }
    ],
    "utter_did_that_help": [
      {
        "text": "Did that help you?"
      }
    ],
    "utter_happy": [
      {
        "text": "Great, carry on!"
      }
    ],
    "utter_goodbye": [
      {
        "text": "Bye"
      }
    ],
    "utter_iamabot": [
      {
        "text": "I am a bot, powered by Rasa."
      }
    ]
  },
  "session_config": {
    "session_expiration_time": 60,
    "carry_over_slots_to_new_session": True
  }
}


print(object(response['intents']))