import json
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
import settings as s

def nlu(text):
	response = s.natural_language_understanding.analyze(
	    text=text,
	    features=[features.Entities(), features.Keywords()])
	return json.dumps(response, indent=2)