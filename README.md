# Gamepad Driver Class 
Gamepad Driver with Shanwan Gamepad, for Teleoperation of Jetracer(Racing car powered by Jetson nano),.

# Usage

### Run gamepad_teleop.py for check (bash)
```bash
python gamepad_teleop.py
# up(left-axis) : throttle up
# down(left-axis) : throttle down
# left(right-axis) : steering left (min:-1)
# right(right-axis) : steerihg right (max:1)
```

### Usage Example (python)
```python
import gamepad_teleop
pad = Gamepad_teleop()
pad = run()
```
