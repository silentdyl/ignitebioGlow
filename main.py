"""
main.py — Entry point for the IgniteTeam BioGlow FLL robot.

How to use
----------
1. Flash pybricks firmware onto your LEGO SPIKE Prime hub.
2. Open this project in the Pybricks IDE (https://code.pybricks.com).
3. Press the hub's centre button to run this program.

The robot will wait for you to press the hub button to select a mission,
then execute it automatically.  Press the left/right buttons to cycle
through missions and the centre button to run the selected mission.
"""

from pybricks.parameters import Button, Color
from pybricks.tools import wait

from robot.utils import (
    make_hub,
    make_drive_base,
    make_attachment_motors,
    make_color_sensors,
)
from robot.missions import mission1, mission2, mission3

# ---------------------------------------------------------------------------
# Robot initialisation
# ---------------------------------------------------------------------------
hub = make_hub()
drive_base = make_drive_base()
attachments = make_attachment_motors()
color_sensors = make_color_sensors()

# List of all missions in run order.
# Add new missions here as (label, module) tuples.
MISSIONS = [
    ("Mission 1", mission1),
    ("Mission 2", mission2),
    ("Mission 3", mission3),
]

# ---------------------------------------------------------------------------
# Mission selector loop
# ---------------------------------------------------------------------------
selected = 0
total = len(MISSIONS)


def show_selection():
    """Display the currently selected mission number on the hub display."""
    hub.display.number(selected + 1)
    hub.light.on(Color.GREEN)


show_selection()

while True:
    pressed = hub.buttons.pressed()

    # Right button → next mission
    if Button.RIGHT in pressed:
        selected = (selected + 1) % total
        show_selection()
        wait(300)

    # Left button → previous mission
    elif Button.LEFT in pressed:
        selected = (selected - 1) % total
        show_selection()
        wait(300)

    # Centre button → run the selected mission
    elif Button.CENTER in pressed:
        label, mission_module = MISSIONS[selected]
        hub.light.on(Color.YELLOW)
        hub.display.char("R")   # "R" for Running
        wait(500)

        mission_module.run(drive_base, attachments)

        hub.light.on(Color.GREEN)
        show_selection()
        wait(500)

    wait(50)
