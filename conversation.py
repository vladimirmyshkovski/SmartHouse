import json
import settings as s







# replace with your own workspace_id
workspace_id = 'f0690275-22cc-4972-af21-df427ea24f13'

def conversation(text):
	response = s.conversation.message(workspace_id=workspace_id, message_input={
		'text': text})
	return json.dumps(response, indent=2)