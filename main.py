# FLASK IMPORTS
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask import session
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required
#######################################
# BOTS IMPORTS 
from app.bots.main_wit import client
from app.bots.natural_language_understanding import nlu
from app.bots.conversation import conversation
from app.bots.text_to_speach import text_to_speach
from app.bots.weather import weather
#######################################
# UTILS IMPORTS
from app.utils.generator import generator
#######################################
# OTHERS IMPORTS
import ujson as json
import requests
import geocoder
#######################################

import os

#from flask_socketio import SocketIO

class SpeachForm(FlaskForm):
    text = TextField('openid', validators = [Required()])

app = Flask(__name__)




@app.route("/", methods=["POST", "GET"])
def hello():
	form = SpeachForm()
	filename = ''
	if request.method == "POST":
		if form.validate_on_submit():
			filename = generator()
			data = json.loads(nlu(form.text.data))
			try:
				text_to_speach(weather(data))
			except:
				pass
			try:
				answer = json.loads(conversation(form.text.data))
				text_to_speach(answer, filename)
			except:
				pass
			return render_template('index.html', form=form, play=True, filename=filename)
	return render_template('index.html', form=form, play=True, filename=filename )


app.config['UPLOAD_FOLDER'] = s.UPLOAD_FOLDER
app.secret_key = s.SECRET_KEY


