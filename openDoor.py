import RPi.GPIO as GPIO
from flask import Flask
from flask import request

import os

HOST = "165.194.27.172"

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def openDoor():
	id = request.form['id']
	print id
	if id == 'ZeroPage':
		os.system("aplay /home/pi/sound/and_open.wav &")	
		execfile("open.py")
		return 'Ok'
	else:
		return 'access denied'

if __name__ == '__main__':
	app.run(HOST,5000)
