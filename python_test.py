# import json

# response = {
#   "version": "3.1",
#   "intents": [
#     "affirm",
#     "bot_challenge",
#     "deny",
#     "goodbye",
#     "greet",
#     "mood_great",
#     "mood_unhappy"
#   ],
#   "responses": {
#     "utter_greet": [
#       {
#         "text": "Hey! How are you?"
#       }
#     ],
#     "utter_cheer_up": [
#       {
#         "text": "Here is something to cheer you up:",
#         "image": "https:\/\/i.imgur.com\/nGF1K8f.jpg"
#       }
#     ],
#     "utter_did_that_help": [
#       {
#         "text": "Did that help you?"
#       }
#     ],
#     "utter_happy": [
#       {
#         "text": "Great, carry on!"
#       }
#     ],
#     "utter_goodbye": [
#       {
#         "text": "Bye"
#       }
#     ],
#     "utter_iamabot": [
#       {
#         "text": "I am a bot, powered by Rasa."
#       }
#     ]
#   },
#   "session_config": {
#     "session_expiration_time": 60,
#     "carry_over_slots_to_new_session": True
#   }
# }

# import requests
# import yaml
# import os

# from pathlib import Path



# url = "https://5005-dc1991lau-rasaboilerpla-f0iz7mqzvh5.ws-eu63.gitpod.io/domain/"
# headers = {"Accept": "application/json"}
# payload = {}

# response = requests.request("GET", url, headers=headers)

# response_data = response.json()

# intents = response_data['intents']

# print(intents)


# { "_id" : ObjectId("630f954cee10660d9142989c"), "sender_id" : "user1", "active_loop" : {  }, "events" : [ { "event" : "action", "timestamp" : 1661965644.1146727, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "action_session_start", "policy" : "null", "confidence" : 1, "action_text" : "null", "hide_rule_turn" : false }, { "event" : "session_started", "timestamp" : 1661965644.1147635, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" } }, { "event" : "action", "timestamp" : 1661965644.114782, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "action_listen", "policy" : "null", "confidence" : "null", "action_text" : "null", "hide_rule_turn" : false }, { "event" : "user", "timestamp" : 1661965644.2887058, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "text" : "hello", "parse_data" : { "intent" : { "name" : "greet", "confidence" : 0.9999985694885254 }, "entities" : [ ], "text" : "hello", "message_id" : "0cc729fdcf0d4e6195a28b8bcfa06b4f", "metadata" : {  }, "text_tokens" : [ [ 0, 5 ] ], "intent_ranking" : [ { "name" : "greet", "confidence" : 0.9999985694885254 }, { "name" : "deny", "confidence" : 7.465182534360792e-7 }, { "name" : "goodbye", "confidence" : 3.240129160531069e-7 }, { "name" : "bot_challenge", "confidence" : 1.8240942267766513e-7 }, { "name" : "mood_unhappy", "confidence" : 1.419943629343834e-7 }, { "name" : "mood_great", "confidence" : 3.712759522045417e-8 }, { "name" : "affirm", "confidence" : 3.1898785834982846e-8 } ], "response_selector" : { "all_retrieval_intents" : [ ], "default" : { "response" : { "responses" : "null", "confidence" : 0, "intent_response_key" : "null", "utter_action" : "utter_None" }, "ranking" : [ ] } } }, "input_channel" : "rest", "message_id" : "0cc729fdcf0d4e6195a28b8bcfa06b4f" }, { "event" : "user_featurization", "timestamp" : 1661965644.9061625, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "use_text_for_featurization" : false }, { "event" : "action", "timestamp" : 1661965644.9061866, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "utter_greet", "policy" : "MemoizationPolicy", "confidence" : 1, "action_text" : "null", "hide_rule_turn" : false }, { "event" : "bot", "timestamp" : 1661965644.9062736, "metadata" : { "utter_action" : "utter_greet", "model_id" : "41ff7787900644ac8573a369540b27d1" }, "text" : "Hey Men", "data" : { "elements" : "null", "quick_replies" : "null", "buttons" : "null", "attachment" : "null", "image" : "null", "custom" : "null" } }, { "event" : "action", "timestamp" : 1661965644.9134498, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "action_listen", "policy" : "MemoizationPolicy", "confidence" : 1, "action_text" : "null", "hide_rule_turn" : false }, { "event" : "user", "timestamp" : 1661965786.3537748, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "text" : "bye", "parse_data" : { "intent" : { "name" : "goodbye", "confidence" : 0.9999991655349731 }, "entities" : [ ], "text" : "bye", "message_id" : "690db4042b434ce09bd32d34026edba5", "metadata" : {  }, "text_tokens" : [ [ 0, 3 ] ], "intent_ranking" : [ { "name" : "goodbye", "confidence" : 0.9999991655349731 }, { "name" : "bot_challenge", "confidence" : 2.8251440653548343e-7 }, { "name" : "mood_unhappy", "confidence" : 2.0199252048769267e-7 }, { "name" : "deny", "confidence" : 1.538343781248841e-7 }, { "name" : "greet", "confidence" : 1.0563811514430199e-7 }, { "name" : "mood_great", "confidence" : 5.7069613035309885e-8 }, { "name" : "affirm", "confidence" : 1.826623652334547e-8 } ], "response_selector" : { "all_retrieval_intents" : [ ], "default" : { "response" : { "responses" : "null", "confidence" : 0, "intent_response_key" : "null", "utter_action" : "utter_None" }, "ranking" : [ ] } } }, "input_channel" : "rest", "message_id" : "690db4042b434ce09bd32d34026edba5" }, { "event" : "user_featurization", "timestamp" : 1661965786.8819559, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "use_text_for_featurization" : false }, { "event" : "action", "timestamp" : 1661965786.8819785, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "utter_goodbye", "policy" : "RulePolicy", "confidence" : 1, "action_text" : "null", "hide_rule_turn" : true }, { "event" : "bot", "timestamp" : 1661965786.8820806, "metadata" : { "utter_action" : "utter_goodbye", "model_id" : "41ff7787900644ac8573a369540b27d1" }, "text" : "Bye", "data" : { "elements" : "null", "quick_replies" : "null", "buttons" : "null", "attachment" : "null", "image" : "null", "custom" : "null" } }, { "event" : "action", "timestamp" : 1661965786.8893251, "metadata" : { "model_id" : "41ff7787900644ac8573a369540b27d1" }, "name" : "action_listen", "policy" : "RulePolicy", "confidence" : 1, "action_text" : "null", "hide_rule_turn" : true } ], "followup_action" : "null", "latest_action" : { "action_name" : "action_listen" }, "latest_action_name" : "action_listen", "latest_event_time" : 1661965786.8893251, "latest_input_channel" : "rest", "latest_message" : { "intent" : { "name" : "goodbye", "confidence" : 0.9999991655349731 }, "entities" : [ ], "text" : "bye", "message_id" : "690db4042b434ce09bd32d34026edba5", "metadata" : {  }, "text_tokens" : [ [ 0, 3 ] ], "intent_ranking" : [ { "name" : "goodbye", "confidence" : 0.9999991655349731 }, { "name" : "bot_challenge", "confidence" : 2.8251440653548343e-7 }, { "name" : "mood_unhappy", "confidence" : 2.0199252048769267e-7 }, { "name" : "deny", "confidence" : 1.538343781248841e-7 }, { "name" : "greet", "confidence" : 1.0563811514430199e-7 }, { "name" : "mood_great", "confidence" : 5.7069613035309885e-8 }, { "name" : "affirm", "confidence" : 1.826623652334547e-8 } ], "response_selector" : { "all_retrieval_intents" : [ ], "default" : { "response" : { "responses" : "null", "confidence" : 0, "intent_response_key" : "null", "utter_action" : "utter_None" }, "ranking" : [ ] } } }, "paused" : false, "slots" : { "session_started_metadata" : "null" } }


test_list = [
    {
      "event": "user",
      "timestamp": 1662557236.5719895,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "Arroz",
      "parse_data": {
        "intent": {
          "name": "nlu_fallback",
          "confidence": 0.3
        },
        "entities": [],
        "text": "Arroz",
        "message_id": "4f22725654ce4cb793f842d72b8712ed",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "nlu_fallback",
            "confidence": 0.3
          },
          {
            "name": "mood_great",
            "confidence": 0.32825520634651184
          },
          {
            "name": "deny",
            "confidence": 0.3205782473087311
          },
          {
            "name": "bot_challenge",
            "confidence": 0.2407679408788681
          },
          {
            "name": "mood_unhappy",
            "confidence": 0.05900577828288078
          },
          {
            "name": "affirm",
            "confidence": 0.039188679307699203
          },
          {
            "name": "goodbye",
            "confidence": 0.007281742990016937
          },
          {
            "name": "greet",
            "confidence": 0.004922280553728342
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "4f22725654ce4cb793f842d72b8712ed"
    },
    {
      "event": "user",
      "timestamp": 1662558048.1198359,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "Arroz",
      "parse_data": {
        "intent": {
          "name": "nlu_fallback",
          "confidence": 0.3
        },
        "entities": [],
        "text": "Arroz",
        "message_id": "46ed2147f6454b1985d305d68efa3c7a",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "nlu_fallback",
            "confidence": 0.3
          },
          {
            "name": "mood_great",
            "confidence": 0.32825520634651184
          },
          {
            "name": "deny",
            "confidence": 0.3205782473087311
          },
          {
            "name": "bot_challenge",
            "confidence": 0.2407679408788681
          },
          {
            "name": "mood_unhappy",
            "confidence": 0.05900577828288078
          },
          {
            "name": "affirm",
            "confidence": 0.039188679307699203
          },
          {
            "name": "goodbye",
            "confidence": 0.007281742990016937
          },
          {
            "name": "greet",
            "confidence": 0.004922280553728342
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "46ed2147f6454b1985d305d68efa3c7a"
    },
    {
      "event": "user",
      "timestamp": 1662559709.5790417,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "bye",
      "parse_data": {
        "intent": {
          "name": "goodbye",
          "confidence": 0.9999991655349731
        },
        "entities": [],
        "text": "bye",
        "message_id": "e90b5c1f36cf40e5ada01d3b2cd73194",
        "metadata": {},
        "text_tokens": [
          [
            0,
            3
          ]
        ],
        "intent_ranking": [
          {
            "name": "goodbye",
            "confidence": 0.9999991655349731
          },
          {
            "name": "bot_challenge",
            "confidence": 2.8251440653548343e-07
          },
          {
            "name": "mood_unhappy",
            "confidence": 2.0199252048769267e-07
          },
          {
            "name": "deny",
            "confidence": 1.538343781248841e-07
          },
          {
            "name": "greet",
            "confidence": 1.0563811514430199e-07
          },
          {
            "name": "mood_great",
            "confidence": 5.7069613035309885e-08
          },
          {
            "name": "affirm",
            "confidence": 1.826623652334547e-08
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "e90b5c1f36cf40e5ada01d3b2cd73194"
    },
    {
      "event": "user",
      "timestamp": 1662559730.9599862,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "hello",
      "parse_data": {
        "intent": {
          "name": "greet",
          "confidence": 0.9999985694885254
        },
        "entities": [],
        "text": "hello",
        "message_id": "71ed672d1acc49d5adecd8f2ecd17e1a",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "greet",
            "confidence": 0.9999985694885254
          },
          {
            "name": "deny",
            "confidence": 7.465182534360792e-07
          },
          {
            "name": "goodbye",
            "confidence": 3.240129160531069e-07
          },
          {
            "name": "bot_challenge",
            "confidence": 1.8240942267766513e-07
          },
          {
            "name": "mood_unhappy",
            "confidence": 1.419943629343834e-07
          },
          {
            "name": "mood_great",
            "confidence": 3.712759522045417e-08
          },
          {
            "name": "affirm",
            "confidence": 3.1898785834982846e-08
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "71ed672d1acc49d5adecd8f2ecd17e1a"
    },
    {
      "event": "user",
      "timestamp": 1662562926.011526,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "hello",
      "parse_data": {
        "intent": {
          "name": "greet",
          "confidence": 0.9999985694885254
        },
        "entities": [],
        "text": "hello",
        "message_id": "1f1eec3a9222447fa92c769b06cef323",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "greet",
            "confidence": 0.9999985694885254
          },
          {
            "name": "deny",
            "confidence": 7.465182534360792e-07
          },
          {
            "name": "goodbye",
            "confidence": 3.240129160531069e-07
          },
          {
            "name": "bot_challenge",
            "confidence": 1.8240942267766513e-07
          },
          {
            "name": "mood_unhappy",
            "confidence": 1.419943629343834e-07
          },
          {
            "name": "mood_great",
            "confidence": 3.712759522045417e-08
          },
          {
            "name": "affirm",
            "confidence": 3.1898785834982846e-08
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "1f1eec3a9222447fa92c769b06cef323"
    },
    {
      "event": "user",
      "timestamp": 1662562960.742476,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "hello",
      "parse_data": {
        "intent": {
          "name": "greet",
          "confidence": 0.9999985694885254
        },
        "entities": [],
        "text": "hello",
        "message_id": "ff55a4da457047aba50c0517e81749f7",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "greet",
            "confidence": 0.9999985694885254
          },
          {
            "name": "deny",
            "confidence": 7.465182534360792e-07
          },
          {
            "name": "goodbye",
            "confidence": 3.240129160531069e-07
          },
          {
            "name": "bot_challenge",
            "confidence": 1.8240942267766513e-07
          },
          {
            "name": "mood_unhappy",
            "confidence": 1.419943629343834e-07
          },
          {
            "name": "mood_great",
            "confidence": 3.712759522045417e-08
          },
          {
            "name": "affirm",
            "confidence": 3.1898785834982846e-08
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "ff55a4da457047aba50c0517e81749f7"
    },
    {
      "event": "user",
      "timestamp": 1662563511.9874957,
      "metadata": {
        "model_id": "41ff7787900644ac8573a369540b27d1"
      },
      "text": "hello",
      "parse_data": {
        "intent": {
          "name": "greet",
          "confidence": 0.9999985694885254
        },
        "entities": [],
        "text": "hello",
        "message_id": "0fcab0fd550c44aba56ee606e6110030",
        "metadata": {},
        "text_tokens": [
          [
            0,
            5
          ]
        ],
        "intent_ranking": [
          {
            "name": "greet",
            "confidence": 0.9999985694885254
          },
          {
            "name": "deny",
            "confidence": 7.465182534360792e-07
          },
          {
            "name": "goodbye",
            "confidence": 3.240129160531069e-07
          },
          {
            "name": "bot_challenge",
            "confidence": 1.8240942267766513e-07
          },
          {
            "name": "mood_unhappy",
            "confidence": 1.419943629343834e-07
          },
          {
            "name": "mood_great",
            "confidence": 3.712759522045417e-08
          },
          {
            "name": "affirm",
            "confidence": 3.1898785834982846e-08
          }
        ],
        "response_selector": {
          "all_retrieval_intents": [],
          "default": {
            "response": {
              "responses": "null",
              "confidence": 0.0,
              "intent_response_key": "null",
              "utter_action": "utter_None"
            },
            "ranking": []
          }
        }
      },
      "input_channel": "rest",
      "message_id": "0fcab0fd550c44aba56ee606e6110030"
    }
  ]
  

a = [
    {'main_color': 'red', 'second_color':'blue'},
    {'main_color': 'yellow', 'second_color':'green'},
    {'main_color': 'yellow', 'second_color':'blue'},
    {'main_color': 'blue', 'second_color':'blue'},
    {'main_color': 'green', 'second_color':'blue'},
    {'main_color': 'red', 'second_color':'blue'},
]

new_list = []
unique_list = []

for i in a:
    if i['main_color'] not in new_list:
        new_list.append(i['main_color'])
        unique_list.append(i)

print(new_list)
print(unique_list)