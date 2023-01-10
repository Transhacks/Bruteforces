from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
import time

A0 = (410) 
AA0 = (1260)
A1 = (170)
AA1 = (660)
A2 = (410)
AA2 =(650)
A3 = (640)
AA3 = (650)
A4 = (170)
AA4 = (860)
A5 = (410)
AA5 = (860)
A6 = (640)
AA6 = (860)
A7 = (170)
AA7 = (1060)
A8 = (410)
AA8 = (1060)
A9 = (640)
AA9 = (1060)
AA = (640)
AAA = (1260)

device = zxtouch("192.168.1.3")

time.sleep(2)

for i in range(8230, -1, -1):
    number_str = str(i).zfill(4)
    
    for digit in number_str:
        x, y = globals()[f"A{digit}"], globals()[f"AA{digit}"]
        
        device.touch(TOUCH_DOWN, 1, x, y)
        time.sleep(0.2)
        device.touch(TOUCH_UP, 1, x, y)
        time.sleep(0.2)
    
    device.touch(TOUCH_DOWN, 1, AA, AAA)
    time.sleep(0.2)
    device.touch(TOUCH_UP, 1, AA, AAA)
    time.sleep(2)
    print(i)
    
