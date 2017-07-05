import json
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
import settings as s

def nlu(text):
	print('IN WATSON : ' + str(text))
	response = s.natural_language_understanding.analyze(
	    text=text,
	    features=[
	    features.Emotion(), features.Concepts(), 
	    features.Categories(), features.Entities(), features.Keywords(),
	    features.SemanticRoles(), features.Relations(), features.Sentiment()])
	return json.dumps(response, indent=2)