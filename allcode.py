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
    if ColorTabEye.color() == Color.YELLOW:
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=120)
        armleft.run_angle(400, -60)
        armright.run_angle(400, -80)
        bot.straight(660)
        bot.turn(-80)
        armright.run_angle(400, 80)
        bot.straight(80)
        armright.run_angle(400, -80)
        armright.run_angle(400, 80)
        armright.run_angle(400, -80)
        bot.straight(-100)
        bot.turn(40)
        bot.straight(-100) 
        armleft.run_angle(400, 60)
        bot.turn(35)
        bot.straight(16) 
        armleft.run_angle(400, -60)
        bot.settings(200, 100)
        bot.straight(-90)  
        bot.settings(100, 90)  
        bot.straight(50)    
        armleft.run_angle(400, -60)
        bot.turn(90)
        bot.straight(320)
        bot.turn(45)
        bot.straight(-180)



    if ColorTabEye.color() == Color.BLUE:
        
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=120)


        bot.straight(370)
        armright.run_angle(-300, 90)
        bot.straight(-370)
        armright.run_angle(300, 90)


    if ColorTabEye.color() == Color.RED:

        bot.settings(straight_speed=600, straight_acceleration=600)
        hub.speaker.play_notes(['C5/5', 'E3/3'], tempo=120)


        bot.straight(1700)

    #use the green tab to use the tree 
    # Add the wait to make sure the tab is out of the sensor's slot to prvent a loop
    if ColorTabEye.color() == Color.GREEN:
        hub.speaker.play_notes(['C3/3', 'E3/3'], tempo=120)
        bot.settings(straight_speed=100, straight_acceleration=200)
        bot.straight(220)
        bot.turn(-50)
        bot.straight(522)
        speed = 20
        bot.turn(50)
        speed = 1
        bot.settings(straight_speed=55, straight_acceleration=70)
        bot.straight(210)
        bot.settings(straight_speed=100, straight_acceleration=220)
        bot.straight(-95)
        speed = 100
        bot.turn(50)
        speed = 30
        bot.straight(-240)
        speed = 100
