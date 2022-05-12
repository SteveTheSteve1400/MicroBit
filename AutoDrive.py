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
    move(1000)
    basic.clear_screen()
    turnR(50)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def move(d: number):
    global e, f
    e = 0
    f = input.compass_heading()
    while e != d:
        number2 = input.compass_heading()
        if number2 <= f and abs(f - number2) >= 20:
            basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
            serial.write_number(f)
            serial.write_number(number2)
            while abs(f - number2) >= 20:
                number2 = input.compass_heading()
                basic.show_leds("""
                            . . . . .
                            . . # . .
                            . . # . .
                            . . # . .
                            . . . . .
                            """)
                serial.write_number(f)
                serial.write_number(number2)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD,0)
                motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 20)
                if abs(f - number2) <= 5:
                    motobit.enable(MotorPower.OFF)
                    basic.clear_screen()
                    break
        elif number2 >= f and abs(f - number2) >= 20:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
            while abs(f - number2) >= 10:
                number2 = input.compass_heading()
                basic.show_leds("""
                    . . # . .
                    . . # . .
                    . . # . .
                    . . # . .
                    . . # . .
                    """)
                serial.write_number(f)
                serial.write_number(number2)
                motobit.enable(MotorPower.OFF)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 20)
                motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 0)
                if abs(f - number2) <= 10:
                    motobit.enable(MotorPower.OFF)
                    basic.clear_screen()
                    break
        else:
            motobit.enable(MotorPower.ON)
            basic.show_leds("""
                                        . . . . .
                                        . . . . .
                                        # # # # #
                                        . . . . .
                                        . . . . .
                                        """)
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 64)
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 64)
            pause(d / 5)
            e = e + d / 5
            motobit.enable(MotorPower.OFF)
# while loop to make it continuious so it adds on
def turnR(b: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
    motobit.enable(MotorPower.OFF)
f = 0
e = 0
number = 0
h = 0
g = 0
direction = "RIGHT"
motobit.enable(MotorPower.OFF)

def on_forever():
    pause(10000)
basic.forever(on_forever)
