# import libraries 
import RPi.GPIO as gpio

from time import sleep ####################


# set pin mapping to BOARD
gpio.setmode(gpio.BOARD)


# turn off channel warnings messages
gpio.setwarnings(False)

# Set GPIO pins as output
ENA=32
ENB=33
gpio.setup(ENA,gpio.OUT)
gpio.setup(ENB,gpio.OUT)

gpio.setup(12,gpio.OUT)
gpio.setup(18,gpio.OUT)


# set GPIO pins as inputs
leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor,gpio.IN)
gpio.setup(rightSensor,gpio.IN)

# turn on left motor
def leftOn():
    gpio.output(12,1)

# turn off left motor
def leftOff():
    gpio.output(12,0)
    
    
# turn on right motor
def rightOn():
    gpio.output(18,1)


#turn off right motor
def rightOff():
    gpio.output(18,0)

# turn off all motors
def stopAll():
    gpio.output(12,0)
    gpio.output(18,0)

speed = 0.10

# main program loop

stopAll()   # make sure all pin are set to off

#Set speed of motors 0-100 means percentage of speed
A=GPIO.PWM(ENA,1000)
A.start(50) #means Run on 50 percent speed
B=GPIO.PWM(ENB,1000)
B.start(50) #means Run on 50 percent speed

while True:
    
    # if left and right sensors are off stop both motors
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor) == 0:  
        leftOff()
        rightOff()
        
    # if both sensors are on then turn both motors on
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==1:
        leftOn()
        rightOn()
        
    # if left sensor is on turn right motor off (pivot left)
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==0:
        leftOn()
        rightOff()
        
    # if right sensor is on turn left motor off (pivot right)
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor)==1:
        leftOff()
        rightOn() 
        
gpio.cleanup()
        
