"""
Utility helpers for the FLL robot drive base and sensors.
These wrappers make mission code more readable.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Button, Color, Stop
from pybricks.tools import wait

import robot.config as cfg


def make_hub():
    """Return an initialised PrimeHub."""
    return PrimeHub()


def make_drive_base():
    """
    Build and return a pybricks DriveBase using the port/geometry settings
    defined in config.py.
    """
    left_motor = Motor(
        getattr(Port, cfg.LEFT_MOTOR_PORT),
        Direction.COUNTERCLOCKWISE,
    )
    right_motor = Motor(
        getattr(Port, cfg.RIGHT_MOTOR_PORT),
        Direction.CLOCKWISE,
    )
    drive_base = DriveBase(
        left_motor,
        right_motor,
        wheel_diameter=cfg.WHEEL_DIAMETER,
        axle_track=cfg.AXLE_TRACK,
    )
    drive_base.settings(
        straight_speed=cfg.STRAIGHT_SPEED,
        straight_acceleration=cfg.STRAIGHT_ACCELERATION,
        turn_rate=cfg.TURN_RATE,
        turn_acceleration=cfg.TURN_ACCELERATION,
    )
    return drive_base


def make_attachment_motors():
    """Return a dict of attachment motors (motor_1, motor_2)."""
    motor_1 = Motor(getattr(Port, cfg.ATTACHMENT_MOTOR_1_PORT))
    motor_2 = Motor(getattr(Port, cfg.ATTACHMENT_MOTOR_2_PORT))
    return {"motor_1": motor_1, "motor_2": motor_2}


def make_color_sensors():
    """Return a dict of left/right color sensors."""
    left = ColorSensor(getattr(Port, cfg.COLOR_SENSOR_LEFT_PORT))
    right = ColorSensor(getattr(Port, cfg.COLOR_SENSOR_RIGHT_PORT))
    return {"left": left, "right": right}


def make_ultrasonic_sensor():
    """Return the ultrasonic distance sensor."""
    return UltrasonicSensor(getattr(Port, cfg.ULTRASONIC_PORT))


def line_follow(drive_base, color_sensors, distance_mm):
    """
    Follow a line for *distance_mm* using proportional control on the left
    color sensor.  The robot stops when the measured distance is reached.

    Args:
        drive_base:     pybricks DriveBase instance.
        color_sensors:  Dict returned by make_color_sensors().
        distance_mm:    How far (in mm) to follow the line.
    """
    drive_base.reset()
    sensor = color_sensors["left"]

    while abs(drive_base.distance()) < distance_mm:
        reflection = sensor.reflection()
        deviation = reflection - cfg.LINE_THRESHOLD
        steering = deviation * cfg.LINE_FOLLOW_GAIN
        drive_base.drive(cfg.LINE_FOLLOW_SPEED, steering)
        wait(10)  # Yield to background tasks while polling

    drive_base.stop()
