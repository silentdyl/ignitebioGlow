#did this on 10/14/2026



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




#hub.speaker.play_notes(['C4/4', 'E4/4'], tempo=120)


# Defines custom colors using HSV:
CYAN = Color(h=180, s=100, v=100)
GRAY = Color(h=0, s=0, v=80)

# Adds them to the detectable color list.
ColorTabEye.detectable_colors([
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.BLACK,
    CYAN,
    GRAY,

])




while True:
    hsv = ColorTabEye.hsv()


    sensed_color = ColorTabEye.hsv()

        # Show the measured color on the hub's center button.
    hub.light.on(sensed_color)


    if ColorTabEye.color() == Color.GRAY:
            hub.speaker.play_notes(['B2/5', 'B3/2'], tempo=1120)
