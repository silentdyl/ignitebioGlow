# ignitebioGlow — IgniteTeam BioGlow FLL Robot

This repository contains the [Pybricks](https://pybricks.com) MicroPython code for the **IgniteTeam BioGlow** robot competing in the FIRST LEGO League (FLL) competition.

## Project structure

```
.
├── main.py                  # Entry point / mission selector
└── robot/
    ├── config.py            # Hardware port assignments and tuning constants
    ├── utils.py             # Drive-base helpers, sensor wrappers, line-follow
    └── missions/
        ├── mission1.py      # Mission 1 sequence
        ├── mission2.py      # Mission 2 sequence
        └── mission3.py      # Mission 3 sequence
```

## Getting started

### Requirements

- [LEGO Education SPIKE Prime](https://education.lego.com/en-us/products/lego-education-spike-prime-set/45678) hub
- [Pybricks firmware](https://pybricks.com/install/) flashed onto the hub
- [Pybricks IDE](https://code.pybricks.com) (runs in Chrome/Edge, no install needed)

### Running the robot

1. Flash the Pybricks firmware onto the SPIKE Prime hub following the [official guide](https://pybricks.com/install/).
2. Open the Pybricks IDE at <https://code.pybricks.com>.
3. Create a new project and copy the contents of this repository into it (or use the IDE's GitHub import feature).
4. Click **Run** (or press the hub's Bluetooth button then the centre button).

### Selecting a mission

| Button | Action |
|--------|--------|
| ← Left  | Previous mission |
| → Right | Next mission |
| ● Centre | Run selected mission |

The hub display shows the current mission number (1–3). The light turns **yellow** while a mission is running and **green** when it is ready for the next selection.

## Adding a new mission

1. Create a new file `robot/missions/mission4.py` (copy an existing mission as a template).
2. Implement the `run(drive_base, attachments)` function.
3. Add the mission to the `MISSIONS` list in `main.py`:
   ```python
   from robot.missions import mission4
   MISSIONS = [
       ...
       ("Mission 4", mission4),
   ]
   ```

## Configuring the robot hardware

Edit `robot/config.py` to match your robot's physical build:

- **Motor ports** – update `LEFT_MOTOR_PORT`, `RIGHT_MOTOR_PORT`, `ATTACHMENT_MOTOR_1_PORT`, `ATTACHMENT_MOTOR_2_PORT`.
- **Sensor ports** – update `GYRO_PORT`, `COLOR_SENSOR_LEFT_PORT`, etc.
- **Wheel geometry** – set `WHEEL_DIAMETER` and `AXLE_TRACK` to your measured values (in mm) for accurate straight/turn distances.
- **Speeds** – tune `STRAIGHT_SPEED`, `TURN_RATE`, etc. to suit your robot's weight and wheel grip.

## Team

**IgniteTeam BioGlow** — FLL Competition Team
