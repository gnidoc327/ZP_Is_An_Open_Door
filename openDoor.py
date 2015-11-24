import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import random
import os

HOST = "165.194.27.172"

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def openDoor():
	id = request.form['id']
	print id
	if id == 'ZeroPage':
		os.system("aplay /home/pi/sound/and_open.wav &")	
		os.system("nohup sudo python /home/pi/zerobot/open.py")
		
		return 'Ok'
	else:
		a = random.random()%1
		
		if a == 0:
			os.system("aplay /home/pi/sound/no_doing1.wav &")
		else:
			os.system("aplay /home/pi/sound/no_doing2.wav &")
		
		return 'access denied'

if __name__ == '__main__':
	app.run(HOST,5000)
