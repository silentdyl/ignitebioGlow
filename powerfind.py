

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




while True:
    voltage = hub.battery.voltage()  # millivolts
    power = int((voltage - 6500) * 100 / (8400 - 6500))
    power = max(0, min(100, power))

    # Green = high charge, red = low charge.
    hue = int(120 * power / 100)
    hub.light.on(Color(h=hue, s=100, v=100))
