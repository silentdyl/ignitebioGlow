"""
Mission 2 — Example mission.

Replace the placeholder movements below with the actual sequence required
for the second mission on the FLL competition table.
"""

from pybricks.tools import wait


def run(drive_base, attachments):
    """
    Execute mission 2.

    Args:
        drive_base:  pybricks DriveBase instance.
        attachments: Dict of attachment motors returned by make_attachment_motors().
    """
    # --- Drive to mission model -----------------------------------------------
    drive_base.straight(500)
    drive_base.turn(90)
    drive_base.straight(200)

    # --- Activate attachment ---------------------------------------------------
    attachments["motor_2"].run_angle(speed=200, rotation_angle=-180)
    wait(500)

    # --- Return to base -------------------------------------------------------
    drive_base.straight(-200)
    drive_base.turn(-90)
    drive_base.straight(-500)

    drive_base.stop()
