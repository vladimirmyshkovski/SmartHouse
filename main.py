from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask import session

from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

import speech_recognition as sr

from main_wit import client

from text_to_speach import text_to_speach
from natural_language_understanding import nlu
import settings as s
import os
from utils import generator
from conversation import conversation
import json
import requests
import geocoder
#from flask_socketio import SocketIO

class SpeachForm(FlaskForm):
    text = TextField('openid', validators = [Required()])

app = Flask(__name__)

USERNAME = "dda5b6bb-a242-4438-b1c9-9ed7edc4f2a6"
PASSWORD = "ft1QDwL4Jp"


@app.route("/", methods=["POST", "GET"])
def hello():
	form = SpeachForm()
	filename = ''
	if request.method == "POST":
		if form.validate_on_submit():
			filename = generator()
			#wit_response = client.message(str(form.text.data))
			c = conversation(form.text.data)
			response = nlu(form.text.data)
			#print(response)
			asd = json.loads(response)
			if (asd['entities'][0]['disambiguation']['subtype'][0]) == 'City':
				if asd['concepts'][0]['text'] == 'Weather' and asd['concepts'][0]['relevance'] >= .9:
					#print(asd['entities'][0]['text'])
					r = requests.get('https://{}:{}@twcservice.eu-gb.mybluemix.net/api/weather/v3/location/search?query={}&language=en-US'.format(USERNAME, PASSWORD, asd['entities'][0]['text']))
					res = r.json()
					#print(res['location'], res['location']['latitude'], res['location']['longitude'])
					#print(res['location']['latitude'][0], res['location']['longitude'][0])
					g = geocoder.google([res['location']['latitude'][0], res['location']['longitude'][0]], method='reverse')
					#print(g.json)
					#r = requests.get('https://{}:{}@twcservice.eu-gb.mybluemix.net/api/weather/v1/geocode/{}/{}/observations.json'.format(USERNAME, PASSWORD, res['location']['latitude'][0], res['location']['longitude'][0]))
					r = requests.get('https://{}:{}@twcservice.eu-gb.mybluemix.net/api/weather/v1/geocode/{}/{}/forecast/daily/7day.json'.format(USERNAME, PASSWORD, res['location']['latitude'][0], res['location']['longitude'][0]))
					res = r.json()
					fields = ['temp', 'pop', 'uv_index', 'narrative', 'phrase_12char', 'phrase_22char', 'phrase_32char']
					print(res['forecasts'][0]['narrative'])
					#print(res['forecasts'][0]['night'])
					print(res['forecasts'][0]['night']['narrative'])
					text_to_speach('by day: ' + str(res['forecasts'][0]['narrative']) + ', at night: ' + str(res['forecasts'][0]['night']['narrative']) , filename)
					#for i in res['metadata']:
					#	print('METADATA : ' + str(i))
					#r = requests.get('https://{}:{}@dda5b6bb-a242-4438-b1c9-9ed7edc4f2a6:ft1QDwL4Jp@twcservice.eu-gb.mybluemix.net:443/'.format(USERNAME, PASSWORD))
			else:
				answer = json.loads(c)
				answer = answer['output']['text'][0]
				#flash('I heard you say: ' + str(form.text.data))
				#flash('Yay, got Wit.ai response: ' + str(wit_response))
				#flash('I understand: ' + response)
				#flash('Answer from bot: ' + str(c))
				flash('You: ' + str(form.text.data))
				flash('Julia: ' + str(answer))
				#text_to_speach(answer, filename)
			return render_template('index.html', form=form, play=True, filename=filename)
	return render_template('index.html', form=form, play=True, filename=filename )


app.config['UPLOAD_FOLDER'] = s.UPLOAD_FOLDER
app.secret_key = s.SECRET_KEY


