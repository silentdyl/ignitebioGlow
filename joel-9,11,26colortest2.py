from pybricks.hubs import PrimeHub  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor  # type: ignore[import-not-found]
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop  # type: ignore[import-not-found]
from pybricks.robotics import DriveBase  # type: ignore[import-not-found]
from pybricks.tools import wait, StopWatch  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor, ColorSensor # type: ignore

hub = PrimeHub()

leftmotor = Motor(Port.F)
rightmotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
armleft = Motor(Port.B)
armright = Motor(Port.E)
ColorTabEye = ColorSensor(Port.A)
Downeye = ColorSensor(Port.C)
bot = DriveBase(leftmotor, rightmotor, wheel_diameter=43, axle_track=95)
#adding this in case the code gets stuck in a loop, it will stop after 2 seconds and 4000 milliseconds of no movement
#bot.settings(stalled_tolerances=(2, 4000)) 

bot.use_gyro(True)
#bot.settings(turn_rate=100, turn_acceleration=500)

#bot.straight(100)
hub.speaker.beep(200, 200)

#Mission emergencyredside
while True:
    # Checks if the detected color is blue
    # Add the wait to make sure the tab is out of the sensor's slot to prvent a loop
    if ColorTabEye.color() == Color.YELLOW:
        wait(2000)
     
        bot.turn(90)
        bot.straight(-100)
       
        
