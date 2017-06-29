from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask import session

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

import speech_recognition as sr
import os
from os import path

from main_wit import client

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
			flash(form.text.data)
			bot_response = client.run_actions('mysession', form.text.data, {})

	return render_template('index.html', form=form)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
