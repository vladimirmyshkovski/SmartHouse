import ujson as json
from ..settings import conversation as c

# replace with your own workspace_id
workspace_id = 'f0690275-22cc-4972-af21-df427ea24f13'

def conversation(text, context):
	response = c.message(workspace_id=workspace_id, message_input={
		'text': text}, context=context)
	return json.dumps(response, indent=2)