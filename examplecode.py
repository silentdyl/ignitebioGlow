#Examples for Code
set up the base
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize the hub
hub = PrimeHub()

# Initialize your left and right motors
# Adjust Direction if a motor needs to spin backward to go forward
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialize the drive base with your wheel diameter (mm) and track width (mm)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Enable the internal gyro for perfectly straight driving and accurate turns
drive_base.use_gyro(True)

# Drive straight forward by 500 millimeters (0.5 meters)
drive_base.straight(500)



                  
