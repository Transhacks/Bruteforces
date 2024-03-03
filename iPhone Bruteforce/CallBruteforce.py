from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
import time

coordinates = [(410, 1260), (170, 660), (410, 650), (640, 650), (170, 860), (410, 860), (640, 860), (170, 1060), (410, 1060), (640, 1060), (640, 1260)]

coord_dict = {str(i): coordinates[i] for i in range(10)}

device = zxtouch("192.168.1.161")
time.sleep(2)

for i in range(9999, -1, -1):
    number_str = str(i).zfill(4)

    for digit in number_str:
        coord = coord_dict[digit]
        device.touch(TOUCH_DOWN, 1, *coord)
        time.sleep(0.2)
        device.touch(TOUCH_UP, 1, *coord)
        time.sleep(0.2)

    device.touch(TOUCH_DOWN, 1, *coordinates[-1])
    time.sleep(0.2)
    device.touch(TOUCH_UP, 1, *coordinates[-1])
    time.sleep(2)
    print(i)
