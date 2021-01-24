# Gamepad Driver Class for Jetson Teleoperation with Shanwan Gamepad.
# Released by Applesquiz (https://github.com/Kanghyun-Kim/gamepad)
# Inspired by the gist by rdb:
# https://gist.github.com/rdb/8864666

# Typical usage example:
#  pad = Gamepad_teleop()
#  pad = run()

import os, struct, array
import traitlets

class Gamepad_teleop(traitlets.HasTraits):
    maps = {'axis':['x', 'y', 'z', 'rz', 'hat0x', 'hat0y'],
            'button':['btn_y', 'btn_b', 'btn_a', 'btn_x', 'btn_xx', 'btn_xxx', 'tl', 'tr', 'tl2', 'tr2', 'select', 'start', 'mode']}
    x = traitlets.Float(default_value=0) #0x00 left=-1, right=1
    y = traitlets.Float(default_value=0) #0x01 up = -1, down = 1
    z = traitlets.Float(default_value=0)
    rz = traitlets.Float(default_value=0)
    btn_y = traitlets.Integer(default_value=0)
    btn_b = traitlets.Integer(default_value=0)
    btn_a = traitlets.Integer(default_value=0)
    btn_x = traitlets.Integer(default_value=0)
    throttle = traitlets.Float(default_value=0)
    steering = traitlets.Float(default_value=0)
    js = None # joystick io.bufferedreader
    
    def __init__(self):
        self.connect()
    
    def connect(self, js='/dev/input/js0'):
        print('Open %s...' % js)
        self.js = open(js, 'rb')
        
    def run(self):
        # Main event loop
        while True:
            self.update()
            
    def update(self):
        event_buf = self.js.read(8)
        if event_buf:
            time, value, event_type, number = struct.unpack('IhBB', event_buf)

            if event_type & 0x01:
                button = self.maps['button'][number]
                if button == "btn_y":
                    self.btn_y = value
                elif button == "btn_b":
                    self.btn_b = value
                elif button == "btn_a":
                    self.btn_a = value
                elif button == "btn_x":
                    self.btn_x = value

            if event_type & 0x02:
                axis = self.maps['axis'][number]
                if axis == "x":
                    self.x = value/32767.0
                elif axis == "y":
                    self.y = value/32767.0
                elif axis == "rz":
                    self.rz = value/32767.0
                elif axis == "z":
                    self.z = value/32767.0
    
    @traitlets.observe('y')
    def monitor_throttle(self, change):
        self.throttle = -change['new']
        print('throttle : ', self.throttle)
    
    @traitlets.observe('z')
    def monitor_steering(self, change):
        self.steering = change['new']
        print('steering : ', self.steering)

if __name__ == '__main__':
    pad = Gamepad_teleop()
    pad.run()
    