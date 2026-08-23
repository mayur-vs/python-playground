import json

event_lex = '{"sessionState": {"intent": {"name": "OrderPizza"}}}'

event_dict_object = json.loads(event_lex)

intent_name = event_dict_object["sessionState"]["intent"]["name"]

print(f"Intent Name is {intent_name}")