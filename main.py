from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

import speech_recognition as sr
import os
from os import path

from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

WIT_AI_KEY = "UZ6QX46MOWTVGUHG4ZLSBVG7ADIJAL7A"  # Wit.ai keys are 32-character uppercase alphanumeric strings


UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['wav'])



class SpeachForm(Form):
    text = TextField('openid', validators = [Required()])

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
	form = SpeachForm()
	if request.method == "POST":
		if form.validate_on_submit():
			flash(form.text)
	return render_template('index.html', form=form)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'





'''
@app.route("/save", methods=["POST", "GET"])
def save():

	if request.method == "POST":
		if 'file' not in request.files:
			flash('No file part')
			print('No file part')
			return redirect(request.url)

		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			print('No selected file')
			return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return '123123'

	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)

	try:
		text = r.recognize_wit(audio, key=WIT_AI_KEY)
		print("Wit.ai thinks you said " + text)
		return text
	except sr.UnknownValueError:
		print("Wit.ai could not understand audio")
		return "Wit.ai could not understand audio"
	except sr.RequestError as e:
		print("Could not request results from Wit.ai service; {0}".format(e))
		return "Could not request results from Wit.ai service; {0}".format(e)

	
'''

