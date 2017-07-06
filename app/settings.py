from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import ConversationV1
import os
from os import path

WEATHER_USERNAME = "dda5b6bb-a242-4438-b1c9-9ed7edc4f2a6"
WEATHER_PASSWORD = "ft1QDwL4Jp"

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))

ALLOWED_EXTENSIONS = set(['wav'])
WIT_AI_KEY = "MTQQIB7UCC4PRWOGDDNDHCYH34DAMYLL"

text_to_speech = TextToSpeechV1(
	username='e7ce4e67-f26d-4d85-afde-56dd9816e67d',
	password='Ag7GeK1iX6Nj',
	x_watson_learning_opt_out=True)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='a334c814-adce-4f1f-b0ea-3ffff5b09598',
    password='0SbC5er0IOg3')

conversation = ConversationV1(
    username='96d73750-dfec-48c3-861a-7760620345f2',
    password='3aTgFvJLC37Z',
    version='2017-04-21')