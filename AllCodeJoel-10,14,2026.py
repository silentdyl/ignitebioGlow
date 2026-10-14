from pybricks.hubs import PrimeHub  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor  # type: ignore[import-not-found]
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop  # type: ignore[import-not-found]
from pybricks.robotics import DriveBase  # type: ignore[import-not-found]
from pybricks.tools import wait, StopWatch  # type: ignore[import-not-found]
from pybricks.pupdevices import Motor, ColorSensor # type: ignore

hub = PrimeHub()
speaker = hub.speaker
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
#adding this in case the code gets stuck in a loop, it will stop after 2 seconds and 4000 milliseconds of no movement
#bot.settings(stalled_tolerances=(2, 4000)) 

#bot.use_gyro(True)
#bot.settings(turn_rate=100, turn_acceleration=500)
#bot.end is the code that stops, not just the end of the code, it is a command that stops
#the robot from moving and ends the program.
#bot.straight(100)
hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=120)

    #use the yellow tab to start

# Define custom colors using HSV:
CYAN = Color(h=200, s=110, v=100)
GRAY = Color(h=0, s=0, v=20)
# Add them to the detectable color list.
ColorTabEye.detectable_colors([
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.BLACK,
    Color.CYAN,
    Color.GRAY

])


while True:



    
    sensed_color = ColorTabEye.hsv()
    
    # Show the measured color on the hub's center button.
    hub.light.on(sensed_color)
    
    #use yellow tab to start
    if ColorTabEye.color() == Color.YELLOW:
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=300)
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

#use white tab to start
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
        
   
    


    #use the blue tab to start
    if ColorTabEye.color() == Color.BLUE:
        
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=300)


        bot.straight(370)
        armright.run_angle(-300, 90)
        bot.straight(-370)
        armright.run_angle(300, 90)


    #use the red tab to start
    if ColorTabEye.color() == Color.RED:

        bot.settings(straight_speed=600, straight_acceleration=400)
        hub.speaker.play_notes(['C5/5', 'E3/7', 'C5/5', 'E3/7'], tempo=300)

        bot.straight(8000)
        bot.turn(10)
        bot.straight(8000)

#use cyan tab to start
    if ColorTabEye.color() == Color.CYAN:
    
            bot.settings(straight_speed=600, straight_acceleration=400)
            hub.speaker.play_notes(['C5/5', 'E3/7', 'C5/5', 'E3/7'], tempo=300)
    
            bot.straight(8000)
            bot.turn(-10)
            bot.straight(8000)

    #use the green tab to start
    # Add the wait to make sure the tab is out of the sensor's slot to prvent a loop
    if ColorTabEye.color() == Color.GREEN:
        hub.speaker.play_notes(['C3/3', 'E3/3'], tempo=300)
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
        bot.straight(300)
        bot.settings(straight_speed=300, straight_acceleration=220)
        bot.turn(45)
        bot.straight(500)
        notes = [
        (392, 200),
        (440, 200),
        (523, 300),
        (440, 200),
        (392, 200),
        (330, 400),
        (392, 200),
        (523, 200),
        (587, 400),
        (600, 200),
        (440, 400),
]
        for frequency, duration in notes:
            speaker.beep(frequency, duration)
    

   
    #use the gray tab to start
    if ColorTabEye.color() == Color.GRAY:
        hub.speaker.play_notes(['C3/2', 'E3/2', 'G3/2'], tempo=400)
        bot.settings(straight_speed=110, straight_acceleration=200)
        bot.straight(160)
        armleft.run_angle(400, 180)
        bot.straight(4000)
        bot.turn(-45)
        armleft.run_angle(400, -18)
        bot.straight(350)
        armright.run_angle(400, 90)
        bot.straight(350)        
