from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
import time

A0 = (410, 1260) 
A1 = (170, 660)
A2 = (410, 650)
A3 = (640, 650)
A4 = (170, 860)
A5 = (410, 860)
A6 = (640, 860)
A7 = (170, 1060)
A8 = (410, 1060)
A9 = (640, 1060)
AA = (640, 1260)

device = zxtouch("192.168.1.9")

time.sleep(2)

for i in range(9999, -1, -1):
    number_str = str(i).zfill(4)
    
    for digit in number_str:
        coord = globals()[f"A{digit}"]
        
        device.touch(TOUCH_DOWN, 1, coord[0], coord[1])
        time.sleep(0.2)
        device.touch(TOUCH_UP, 1, coord[0], coord[1])
        time.sleep(0.2)

    device.touch(TOUCH_DOWN, 1, AA[0], AA[1])
    time.sleep(0.2)
    device.touch(TOUCH_UP, 1, AA[0], AA[1])
    time.sleep(2)
    print(i)
