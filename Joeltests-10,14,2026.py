#Blue and Red Side Code


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
leftmotor.control.limits(1000, 1000, 120)
rightmotor.control.limits(1000, 1000, 120)
leftmotor.control.limits(torque=120)
rightmotor.control.limits(torque=120)
armleft.control.limits(torque=120)
#adding this in case the code gets stuck in a loop, it will stop after 2 seconds and 4000 milliseconds of no movement
#bot.settings(stalled_tolerances=(2, 4000)) 
#coach dylan, this made the code quit with an error, so I commented it out.  




hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=120)


# Defines custom colors using HSV:
CYAN = Color(h=195, s=50, v=100)

# Adds them to the detectable color list.
ColorTabEye.detectable_colors([
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.BLACK,
    Color.MAGENTA

])
while True:

    
    
    
    
    if ColorTabEye.color() == Color.YELLOW:
        #Mission ### -- ????
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=120)
        bot.settings(straight_speed=100, straight_acceleration=200)
        armleft.run_angle(400, -100)
        armright.run_angle(400, -80)
        bot.straight(635)
        bot.turn(-80)
        armright.run_angle(400, 80)
        bot.straight(45)
        armright.run_angle(400, -70)
        armright.run_angle(400, 70)
        armright.run_angle(400, -70)
        bot.straight(-65)
        bot.turn(40)
        bot.straight(-100) 
        armleft.run_angle(400, 100)
        bot.turn(35)
        bot.straight(16) 
        armleft.run_angle(400, -70)
        bot.straight(-90)  
        bot.straight(50)    
        armleft.run_angle(400, -70)
        bot.turn(90)
        bot.straight(320)
        bot.turn(40)
        bot.settings(straight_speed=90, straight_acceleration=700)        
        bot.straight(-220)
        bot.settings(straight_speed=100, straight_acceleration=220)   
        bot.straight(220)
        bot.turn(45)
        bot.curve(radius=600, angle=230)
        #takes you back to blue side of the field
        
   
    


    #use the blue tab to start
    if ColorTabEye.color() == Color.BLUE:
        
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=120)


        bot.straight(370)
        armright.run_angle(-300, 90)
        bot.straight(-370)
        armright.run_angle(300, 90)


    #use the red tab to start - EMERGENCY BLUE TO RED
    if ColorTabEye.color() == Color.RED:

#        bot.settings(straight_speed=1000, straight_acceleration=700)
        hub.speaker.play_notes(['C5/5', 'E3/7', 'C5/5', 'E3/7'], tempo=120)
        bot.settings(straight_speed=600, straight_acceleration=600)
        bot.straight(800)
        #how do we speed the code up? 
        bot.curve(radius=200, angle=20)
        bot.straight(800)

    #use the green tab to start
    # Add the wait to make sure the tab is out of the sensor's slot to prvent a loop
    if ColorTabEye.color() == Color.GREEN:
        #Mission 9 - Research Platform Mission 15, Part 2 - Garden Skylight
        hub.speaker.play_notes(['C3/3', 'E3/3'], tempo=120)
        bot.settings(straight_speed=100, straight_acceleration=200)
        bot.straight(220)
        bot.turn(-50)   
        bot.straight(520)
        bot.turn(50)
        bot.settings(straight_speed=150, straight_acceleration=100)
        bot.straight(200)
        bot.settings(straight_speed=100, straight_acceleration=220)
        bot.straight(-120)
        bot.turn(60)
        bot.straight(-190)
        bot.turn(30)
        bot.straight(-70)
        bot.straight(350)
        bot.settings(straight_speed=300, straight_acceleration=220)
        bot.turn(45)
        bot.straight(500)

    #use the white tab to start 
    if ColorTabEye.color() == Color.WHITE:

        hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=100)
        armleft.control.limits(torque=250)
        bot.settings(straight_speed=150, straight_acceleration=250)
        bot.straight(250)
        armleft.run_angle(400, 90, wait=False)
        armright.run_angle(400,-90)
        bot.settings(straight_speed=300, straight_acceleration=250)
        bot.straight(-250)
        armleft.run_angle(400, -90)
        bot.straight(300)
        armleft.run_angle(400, 90)
        bot.straight(-250)

        bot.turn(-50)
        armleft.run_angle(400, -18)
        bot.straight(300)
        armright.run_angle(400, 90)
        bot.straight(-350)

    if ColorTabEye.color() == Color.ORANGE:
        hub.speaker.play_notes(['C9/4', 'E9/4'], tempo=180)

    if ColorTabEye.color() == Color.MAGENTA:
        hub.speaker.play_notes(['C1/4', 'E1/4'], tempo=180)
