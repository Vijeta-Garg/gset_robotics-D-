#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


from pybricks.nxtdevices import LightSensor


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.




# Create your objects here.


brob = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
light_sensor = LightSensor(Port.S2)
color_sensor = ColorSensor(Port.S1)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


lastDeviation = 0
WHITE = 75
BLACK = 0
THRESHOLD = (BLACK + WHITE) / 2
SPEED = 60
kP = 1.4
kD = 0.6


while True:
    deviation = light_sensor.reflection()-THRESHOLD
    turn_rate = kP * deviation + kD * (deviation - lastDeviation)
    lastDeviation = deviation
    if(color_sensor.color() == Color.RED):
        break
    else:
        robot.drive(SPEED, turn_rate)
    #brob.screen.print(light_sensor.reflection())
    wait(10)


robot.stop()
brob.speaker.beep()
wait(10)

