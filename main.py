from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask import session

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

import speech_recognition as sr

from main_wit import client

from text_to_speach import text_to_speach
from natural_language_understanding import nlu
import settings as s



class SpeachForm(Form):
    text = TextField('openid', validators = [Required()])

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
	form = SpeachForm()
	if request.method == "POST":
		if form.validate_on_submit():
			#wit_response = client.message(str(form.text.data))
			#flash('I heard you say: ' + str(form.text.data))
			#flash('Yay, got Wit.ai response: ' + str(wit_response))
			#text_to_speach(form.text.data)
			r = str('I understand: ') + nlu(form.text.data)
			return render_template('index.html', form=form, play=True, r=r)
	return render_template('index.html', form=form)


app.config['UPLOAD_FOLDER'] = s.UPLOAD_FOLDER
app.secret_key = s.SECRET_KEY
