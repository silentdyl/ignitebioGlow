"""
Robot hardware configuration for the FLL competition robot.
Update port assignments and motor/sensor settings to match your physical build.
"""

# Drive base motor ports
LEFT_MOTOR_PORT = "A"
RIGHT_MOTOR_PORT = "B"

# Attachment motor ports
ATTACHMENT_MOTOR_1_PORT = "C"
ATTACHMENT_MOTOR_2_PORT = "D"

# Sensor ports
# Note: the SPIKE Prime hub has a built-in IMU, so no external gyro port is needed.
COLOR_SENSOR_LEFT_PORT = "S2"
COLOR_SENSOR_RIGHT_PORT = "S3"
ULTRASONIC_PORT = "S4"

# Drive base geometry (update to match your robot's measurements in mm/degrees)
WHEEL_DIAMETER = 56        # mm
AXLE_TRACK = 117           # mm (distance between the two drive wheels)

# Drive speeds (deg/s)
STRAIGHT_SPEED = 200
STRAIGHT_ACCELERATION = 400
TURN_RATE = 150
TURN_ACCELERATION = 300

# Line-following parameters
LINE_THRESHOLD = 50        # Reflected light % threshold (black < threshold < white)
LINE_FOLLOW_SPEED = 100    # mm/s
LINE_FOLLOW_GAIN = 1.2     # Proportional gain for line following
