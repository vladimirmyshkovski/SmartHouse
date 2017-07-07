import ujson as json
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
from ..settings import natural_language_understanding as n

def nlu(text):
	print('IN WATSON : ' + str(text))
	response = n.analyze(
	    text=text,
	    features=[
	    features.Emotion(), features.Concepts(), 
	    features.Categories(), features.Entities(), features.Keywords(),
	    features.SemanticRoles(), features.Relations(), features.Sentiment()],
	    language='en')
	return json.dumps(response, indent=2)