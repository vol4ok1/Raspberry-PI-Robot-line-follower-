from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

bd = BlueDot()
robot = Robot(left=(18, 17), right=(24, 23))

def move(pos):
    if pos.top:a
        robot.forward(pos.distance)
    elif pos.bottom:
        robot.backward(pos.distance)
    elif pos.left:
        robot.left(pos.distance)
    elif pos.right:
        robot.right(pos.distance)

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()

Linijos sensoriaus valdymas:

import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)

leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor,gpio.IN)
gpio.setup(rightSensor,gpio.IN)

def leftOn():
    gpio.output(12,1)

def leftOff():
    gpio.output(12,0)
    
    
def rightOn():
    gpio.output(16,1)

def rightOff():
    gpio.output(16,0)

def stopAll():
    gpio.output(12,0)
    gpio.output(16,0)

stopAll()  

while True:
    
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor) == 0:  
        leftOff()
        rightOff()
        
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==1:
        leftOn()
        rightOn()
        
        if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==0:
        leftOn()
        rightOff()
        
        if gpio.input(leftSensor)==0 and gpio.input(rightSensor)==1:
        leftOff()
        rightOn() 
        
gpio.cleanup()
