from pybricks.hubs import PrimeHub  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor  # type: ignore[import-not-found]
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop  # type: ignore[import-not-found]
from pybricks.robotics import DriveBase  # type: ignore[import-not-found]
from pybricks.tools import wait, StopWatch  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor, ColorSensor # type: ignore
 

hub = PrimeHub()

leftmotor = Motor(Port.F)
rightmotor = Motor(Port.D)
armleft = Motor(Port.B)
armright = Motor(Port.E)
ColorTabEye = ColorSensor(Port.A)
Downeye = ColorSensor(Port.C)
bot = DriveBase(leftmotor, rightmotor, wheel_diameter=43, axle_track=95)
#adding this in case the code gets stuck in a loop, it will stop after 2 seconds and 4000 milliseconds of no movement
#bot.settings(stalled_tolerances=(2, 4000)) 

#bot.use_gyro(True)
#bot.settings(turn_rate=100, turn_acceleration=500)
#bot.end is the code that stops, not just the end of the code, it is a command that stops
#the robot from moving and ends the program.
#bot.straight(100)
hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=120)
while True:
    #use the green tab to use the tree 
    # Add the wait to make sure the tab is out of the sensor's slot to prvent a loop
    if ColorTabEye.color() == Color.GREEN:
        
        wait(1500)
        bot.settings(straight_speed=100, straight_acceleration=200)
        bot.straight(220)
        bot.turn(-50)
        bot.straight(525)
        speed = 20
        bot.turn(50)
        wait(1500)
        speed = 1
        bot.settings(straight_speed=40, straight_acceleration=60)
        bot.straight(200)
        
        #back up to farm
        bot.settings(straight_speed=100, straight_acceleration=200)
        bot.straight(-200)
        speed = 100
        bot.turn(90)
        speed = 30
        bot.straight(-240)
        speed = 100
