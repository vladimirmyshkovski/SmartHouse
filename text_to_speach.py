# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1



text_to_speech = TextToSpeechV1(
	username='e7ce4e67-f26d-4d85-afde-56dd9816e67d',
	password='Ag7GeK1iX6Nj',
	x_watson_learning_opt_out=True)  # Optional flag

	#print(json.dumps(text_to_speech.voices(), indent=2))

def text_to_speach(text):
	with open(join(dirname(__file__), '../resources/output.wav'),
	          'wb') as audio_file:
	    audio_file.write(
	        text_to_speech.synthesize('I heard you say ' + str(text), accept='audio/wav',
	                                  voice="en-US_AllisonVoice"))

	#print(
	#    json.dumps(text_to_speech.pronunciation(
	#        'Watson', pronunciation_format='spr'), indent=2))

	#print(json.dumps(text_to_speech.customizations(), indent=2))

