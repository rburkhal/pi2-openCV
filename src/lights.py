#!/usr/bin/env python
# first line points to path for python

# we import the webpy library
import web

import RPi.GPIO as GPIO

#dont bug me with warnings
GPIO.setwarnings(False)

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channels
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

urls = ('/','root')
app = web.application(urls,globals())
 
class root:
 
    def __init__(self):
        self.hello = "snakes on a pie!"
 
    def GET(self):
        getInput = web.input(turn="")
        kommando = str(getInput.turn)
        if kommando == "on":
            #    set RPi board pins high
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(16, GPIO.HIGH)
            return "Lights on"
        if kommando == "off":
            #    set RPi board pins low
            GPIO.output(18, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
            return "Lights off"
 
if __name__ == "__main__":
        app.run()
