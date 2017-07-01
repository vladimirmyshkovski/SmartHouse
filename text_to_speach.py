# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import settings as s 
from utils import generator

#text_to_speech = TextToSpeechV1(
#	username='e7ce4e67-f26d-4d85-afde-56dd9816e67d',
#	password='Ag7GeK1iX6Nj',
#	x_watson_learning_opt_out=True)  # Optional flag


def text_to_speach(text):
	filename = generator()
	print(json.dumps(s.text_to_speech.voices(), indent=2))

	with open(join(dirname(__file__), 'static/resources/{}.wav'.format(filename)),
	          'wb') as audio_file:
	    audio_file.write(
	        s.text_to_speech.synthesize('I heard you say: ' + str(text), accept='audio/wav',
	                                  voice="en-US_AllisonVoice"))
	print(
	    json.dumps(s.text_to_speech.pronunciation(
	        'Watson', pronunciation_format='spr'), indent=2))

	print(json.dumps(s.text_to_speech.customizations(), indent=2))

	return filename

