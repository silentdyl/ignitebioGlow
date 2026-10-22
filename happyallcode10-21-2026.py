
###########   ###       ###   #########         ########      ##########      ############
###########   ###### ######   ############    ############    ############    ############
    ###       ###### ######   ###      ###    ###      ###    ###      ###        ####
    ###       ### ##### ###   ############    ###      ###    ############        ####
    ###       ###  ###  ###   #########       ###      ###    ##########          ####
    ###       ###   #   ###   ###             ###      ###    ###   ###           ####
###########   ###       ###   ###             ############    ###    ###          ####
###########   ###       ###   ###               ########      ###     ###         ####

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
leftmotor.control.limits(torque=120)
rightmotor.control.limits(torque=120)
armleft.control.limits(1000, 1000, 250)
armright.control.limits(1000, 1000, 250)


#HubCodes, the different codes saved to the robot. Each code is saved on GitHub.

#File one = Mission Codes        🟨 ⬜️ ⬜️ ⬜️ ⬜️ 

#File two = Test Codes           ⬜️ 🟨 ⬜️ ⬜️ ⬜️ 

#File three = Battary Check Code ⬜️ ⬜️ 🟨 ⬜️ ⬜️ 

#File four = Random Code Tests   ⬜️ ⬜️ ⬜️ 🟨 ⬜️ 

#File five = Song Codes          ⬜️ ⬜️ ⬜️ ⬜️ 🟨

hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=300)
# Define custom colors using HSV:
CYAN = Color(h=220, s=120, v=100)

# Add them to the detectable color list.
ColorTabEye.detectable_colors([
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.BLACK,
    Color.CYAN,
    

])



# 5x5 faces for the SPIKE Prime hub display.
# 1 = lit pixel, 0 = unlit pixel.

FACES = {
    # Animated waiting faces
    "WAIT_A": (
        "01010",
        "01010",
        "00000",
        "10001",
        "01110",
    ),

    "WAIT_B": (
        "00000",
        "00000",
        "00000",
        "10001",
        "01110",
    ),

    # A different static face for every tab color
    "WHITE": (
        "01010",
        "01010",
        "00000",
        "10001",
        "01110",
    ),
    "CYAN": (
        "11111",
        "01010",
        "00000",
        "10101",
        "01010",
    ),
    "GREEN": (
        "01010",
        "00000",
        "01010",
        "11111",
        "01010",
    ),
    "YELLOW": (
        "01010",
        "01010",
        "00000",
        "01110",
        "01010",
    ),
    "RED": (
        "10001",
        "01010",
        "00000",
        "01110",
        "10001",
    ),
    "BLUE": (
        "01010",
        "10001",
        "00000",
        "01110",
        "10001",
    ),
}



# Draw every pixel, including turning old pixels off.
def show_face(name):
    pattern = FACES[name]

    for y in range(5):
        for x in range(5):
            brightness = 100 if pattern[y][x] == "1" else 0
            hub.display.pixel(x, y, brightness)


# Read the sensor frequently and blink while waiting.
while True:
    detected_color = ColorTabEye.color()

    # None or BLACK means no mission tab is being recognized.
    if detected_color is None or detected_color == Color.BLACK:

        # Eyes open
        show_face("WAIT_A")

        # Check for a tab during the open-eye pause.
        for _ in range(20):
            wait(500)
            detected_color = ColorTabEye.color()

            if detected_color is not None and detected_color != Color.BLACK:
                break

        # If a tab appeared, skip the blink and run its mission.
        if detected_color is not None and detected_color != Color.BLACK:
            pass
        else:
            # Eyes closed: blink for 0.2 seconds.
            show_face("WAIT_B")

            for _ in range(4):
                wait(50)
                detected_color = ColorTabEye.color()

                if detected_color is not None and detected_color != Color.BLACK:
                    break

            # Go back to the top to check the sensor again.
            if detected_color is None or detected_color == Color.BLACK:
                continue

    # Your six mission branches go here.

    # Your six color mission checks go below this line.


#           /\_/\   _
#          ( O.O ) // 
#           )   ( ||
#          (|| ||)//
 
############        ###############     ############
###############     ###############     ###############
####       ####     ###                 ###        ####
###         ###     ###                 ###         ###
####       ####     ##########          ###         ###
###############     ##########          ###         ###
############        ###                 ###         ###
###     ####        ###                 ###         ###
###      ####       ###                 ###        ####
###       ####      ###############     ###############
###        ####     ###############     ############


  ###########       ###############     ############        ###############
###############     ###############     ###############     ###############
####       ####           ###           ###        ####     ###
######                    ###           ###         ###     ###
  ##########              ###           ###         ###     ##########
        #######           ###           ###         ###     ##########
           ####           ###           ###         ###     ###
####       ####           ###           ###        ####     ###
###############     ###############     ###############     ###############
  ###########       ###############     ############        ###############


    #     #  #     #  #######  #######  #######
    #     #  #     #     #        #     #
    #  #  #  #     #     #        #     ###
    # # # #  #######     #        #     #
    ##   ##  #     #     #        #     #
     #   #   #     #  #######     #     #######

    if detected_color == Color.WHITE:
        show_face("WHITE")
        hub.light.on(Color(h=0, s=0, v=100))
        hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=250)
        bot.settings(straight_speed=150, straight_acceleration=200)
        armleft.run_angle(400, 90, wait=False)
        armright.run_angle(400, -90)
        bot.straight(340)
        armleft.run_angle(400, -90, wait=False)
        armright.run_angle(400, 90)
        bot.settings(straight_speed=300, straight_acceleration=250)
        bot.straight(-90)
        armleft.run_angle(400, 90, wait=False)
        armright.run_angle(400, -90)
        bot.straight(90)
        armleft.run_angle(400, -90, wait=False)
        armright.run_angle(400, 90)
        bot.straight(-1000)
        armleft.run_angle(400, 90, wait=False)
        armright.run_angle(400, -90)
        armleft.run_angle(400, -90, wait=False)
        armright.run_angle(400, 90)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        (bot.stop())
        


     #####   #     #     #     #     #
    #     #   #   #     # #    ##    #
    #          # #     #   #   # #   #
    #           #     #######  #  #  #
    #     #     #     #     #  #   # #
     #####      #     #     #  #    ##

    if detected_color == Color.CYAN:
        show_face("CYAN")
        hub.light.on(Color(h=180, s=100, v=100))
        bot.settings(straight_speed=100, straight_acceleration=200)
        hub.speaker.play_notes(['C3/3', 'E3/7', 'C5/5'], tempo=250)
    
        bot.straight(700)
        bot.turn(45)
        bot.straight(30)
        bot.turn(90)
        bot.turn(-90)
        bot.straight(-40)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        (bot.stop())

   
   
     #####   ######   #######  #######  #     #
    #     #  #     #  #        #        ##    #
    #        ######   ###      ###      # #   #
    #   ###  #   #    #        #        #  #  #
    #     #  #    #   #        #        #   # #
     #####   #     #  #######  #######  #    ##

    if detected_color == Color.GREEN:
        show_face("GREEN")
        hub.light.on(Color(h=120, s=100, v=100))
        hub.speaker.play_notes(['C3/3', 'E3/3'], tempo=250)
        bot.settings(straight_speed=150, straight_acceleration=200)
        bot.straight(220)
        (bot.stop())
        bot.turn(-50)   
        bot.straight(520)
        (bot.stop())
        bot.turn(50)
        bot.settings(straight_speed=100, straight_acceleration=100)
        bot.straight(200)
        (bot.stop())
        bot.settings(straight_speed=150, straight_acceleration=220)
        bot.straight(-120)
        bot.turn(60)
        bot.straight(-190)
        bot.turn(20)
        bot.settings(straight_speed=400, straight_acceleration=300)
        bot.straight(-70)
        bot.straight(300)
        bot.settings(straight_speed=300, straight_acceleration=220)
        bot.turn(45)
        bot.straight(500)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        (bot.stop())
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

    #####    #        #     #  #######
    #    #   #        #     #  #
    ######   #        #     #  ###
    #     #  #        #     #  #
    #     #  #        #     #  #
    ######   #######   #####   #######

#use blue doubled over

##########          ###                 ###         ###     ###############
############        ###                 ###         ###     ###############
###      ###        ###                 ###         ###     ###
###      ###        ###                 ###         ###     ###
############        ###                 ###         ###     #########
###############     ###                 ###         ###     #########
###        ####     ###                 ###         ###     ###
###         ###     ###                 ####       ####     ###
###############     ###############     ###############     ###############
#############       ###############       ###########       ###############


  ###########       ###############     ############        ###############
###############     ###############     ###############     ###############
####      #####           ###           ###        ####     ###
######                    ###           ###         ###     ###
  ##########              ###           ###         ###     #########
       ########           ###           ###         ###     #########
            ###           ###           ###         ###     ###
####       ####           ###           ###        ####     ###
###############     ###############     ###############     ###############
  ###########       ###############     ############        ###############




    #     #  #######  #        #         #####   #     #
     #   #   #        #        #        #     #  #     #
      # #    ###      #        #        #     #  #  #  #
       #     #        #        #        #     #  # # # #
       #     #        #        #        #     #  ##   ##
       #     #######  #######  #######   #####    #   #
    
    if detected_color == Color.YELLOW:
        show_face("YELLOW")
        hub.light.on(Color(h=60, s=100, v=100))
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=250)
        bot.settings(straight_speed=180, straight_acceleration=600)
        armleft.run_angle(400, -100)
        armright.run_angle(400, -80)
        bot.straight(625)
        bot.turn(-80)
        bot.settings(straight_speed=150, straight_acceleration=250)
        armright.run_angle(400, 80)
        bot.straight(35)
        armright.run_angle(400, -70)
        armright.run_angle(400, 70)
        armright.run_angle(400, -70)
        bot.straight(-75)
        bot.turn(40)
        bot.straight(-90) 
        armleft.run_angle(400, 120)
        bot.turn(35)
        bot.straight(14) 
        armleft.run_angle(400, -90)
        bot.straight(-90)
        armleft.run_angle(400, -50) 
        bot.straight(50)    
        armleft.run_angle(400, 70)
        bot.turn(80)
        armleft.run_angle(400, -190)
        bot.straight(300)
        bot.turn(35)
        bot.settings(straight_speed=80, straight_acceleration=800)        
        bot.straight(-230)
        bot.settings(straight_speed=100, straight_acceleration=220)   
        bot.straight(250)
        bot.turn(40)
        bot.straight(230)
        bot.turn(-70)
        bot.settings(straight_speed=500, straight_acceleration=500)   
        bot.straight(900)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        #bot.curve(radius=600, angle=230)
        (bot.stop())
        #takes you back to blue side of the field



    ######   #######  ######
    #     #  #        #     #
    ######   ###      #     #
    #   #    #        #     #
    #    #   #        #     #
    #     #  #######  ######

    
    if detected_color == Color.RED:
        show_face("RED")
        hub.light.on(Color(h=0, s=100, v=100))
        bot.settings(straight_speed=600, straight_acceleration=400)
        hub.speaker.play_notes(['C5/5', 'E3/7', 'C5/5', 'E3/7'], tempo=250)
        bot.straight(1000)
        bot.turn(10)
        bot.straight(1000)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        (bot.stop())
   

    #####    #        #     #  #######
    #    #   #        #     #  #
    ######   #        #     #  ###
    #     #  #        #     #  #
    #     #  #        #     #  #
    ######   #######   #####   #######

    if detected_color == Color.BLUE:
        show_face("BLUE")
        hub.light.on(Color(h=240, s=100, v=100))
        hub.speaker.play_notes(['C5/5', 'E5/5'], tempo=250)
        bot.straight(370)
        armright.run_angle(-300, 90)
        armright.run_angle(300, 90)
        bot.straight(-380)
        armleft.reset_angle(0, wait=False)
        armright.reset_angle(0) 
        (bot.stop()) 
