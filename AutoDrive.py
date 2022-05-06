# Add your Python code here. E.g.
from microbit import *
 # Enable motor driver

c = 0
b= 0
def turnL(a: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 40)
    pause(a)
    motobit.enable(MotorPower.OFF)

def on_button_pressed_a():
    motobit.enable(MotorPower.OFF)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    c = input.acceleration(Dimension.X)
    move(51, 7000)
    turnR(590)
    move(51, 4700)
    turnL(590)
    move(51, 4700)
    turnR(590)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def move(c: number, d: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 64)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, c)
    pause(d)
    motobit.enable(MotorPower.OFF)
    
def turnR(b: number):
    number = input.acceleration(Dimension.X)
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
    while(c!=number):
        pass
    motobit.enable(MotorPower.OFF)

    
    
    
