from pybricks.hubs import PrimeHub  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor  # type: ignore[import-not-found]
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop  # type: ignore[import-not-found]
from pybricks.robotics import DriveBase  # type: ignore[import-not-found]
from pybricks.tools import wait, StopWatch  # type: ignore[import-not-found]

hub = PrimeHub()

leftmotor = Motor(Port.F)
rightmotor = Motor(Port.D)
armleft = Motor(Port.B)
armright = Motor(Port.E)

bot = DriveBase(leftmotor, rightmotor,wheel_diameter=43, axle_track=95)
#adding this in case the code gets stuck in a loop, it will stop after 2 seconds and 4000 milliseconds of no movement
bot.settings(stalled_tolerances=(2, 4000)) 

bot.use_gyro(True)
#bot.settings(turn_rate=100, turn_acceleration=500)

#bot.straight(100)
hub.speaker.beep()

#Mission TabBlueSideRed

bot.straight(10)
bot.turn(-90)
bot.straight(470)
bot.turn(-675)
armright.run_angle(30,50)
bot.straight(210)
bot.turn(90)
armright.run_angle(15,50)
    
