"""
Mission 1 — Example mission.

Replace the placeholder movements below with the actual sequence required
for the first mission on the FLL competition table.
"""

from pybricks.tools import wait


def run(drive_base, attachments):
    """
    Execute mission 1.

    Args:
        drive_base:  pybricks DriveBase instance.
        attachments: Dict of attachment motors returned by make_attachment_motors().
    """
    # --- Drive to mission model -----------------------------------------------
    drive_base.straight(300)   # Drive 300 mm forward
    drive_base.turn(-45)        # Turn 45 degrees to the right

    # --- Activate attachment ---------------------------------------------------
    attachments["motor_1"].run_angle(speed=300, rotation_angle=360)

    # --- Return to base -------------------------------------------------------
    drive_base.turn(45)
    drive_base.straight(-300)

    drive_base.stop()
