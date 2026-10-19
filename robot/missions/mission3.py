"""
Mission 3 — Example mission.

Replace the placeholder movements below with the actual sequence required
for the third mission on the FLL competition table.
"""

from pybricks.tools import wait


def run(drive_base, attachments):
    """
    Execute mission 3.

    Args:
        drive_base:  pybricks DriveBase instance.
        attachments: Dict of attachment motors returned by make_attachment_motors().
    """
    # --- Drive to mission model -----------------------------------------------
    drive_base.straight(400)
    drive_base.turn(-90)
    drive_base.straight(150)
    drive_base.turn(90)
    drive_base.straight(100)

    # --- Activate both attachments simultaneously ------------------------------
    attachments["motor_1"].run_angle(speed=300, rotation_angle=180, wait=False)
    attachments["motor_2"].run_angle(speed=300, rotation_angle=180)
    wait(300)

    # --- Return to base -------------------------------------------------------
    drive_base.straight(-100)
    drive_base.turn(-90)
    drive_base.straight(-150)
    drive_base.turn(90)
    drive_base.straight(-400)

    drive_base.stop()
