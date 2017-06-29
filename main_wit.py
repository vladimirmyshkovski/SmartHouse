from wit import Wit
from flask import session


WIT_AI_KEY = "MTQQIB7UCC4PRWOGDDNDHCYH34DAMYLL"

def say(session_id, context, msg):
	print(msg)
	session['answer'] = msg
	return msg
	
actions = {
    'say': say,
}

client = Wit(access_token=WIT_AI_KEY, actions=actions)