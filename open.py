import RPi.GPIO as GPIO
import time

#en_pin = 18 
pwm_pin = 23

GPIO.setmode(GPIO.BCM)
#GPIO.setup(en_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

p = GPIO.PWM(pwm_pin, 50)

p.start(0)
#		GPIO.output(en_pin, GPIO.HIGH)
p.ChangeDutyCycle(12)
time.sleep(2)
p.ChangeDutyCycle(0.5)
time.sleep(2)
p.stop()
GPIO.cleanup()

