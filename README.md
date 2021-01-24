# Gamepad Driver Class 
For Jetracer, Jetson Teleoperation with Shanwan Gamepad.

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
