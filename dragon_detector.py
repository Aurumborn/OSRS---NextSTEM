import numpy as np
import cv2
import time
from directmouse import on_click, check_mouse
from grabscreen import grab_screen                                      # new grab_screen function, its way faster for FPS
from grabkeys import key_check
import os
from pynput import mouse
from pynput.mouse import Button, Controller

dragon_dict = {}
for i,b in enumerate(boxes[0]):
    if classes[0][i] == 3 or classes[0][i] == 6 or classes[0][i] == 8:
        if scores[0][i] > 0.5:
            mid_x = (boxes[0][i][3] + boxes[0][i][1]) / 2
            mid_y = (boxes[0][i][2] + boxes[0][i][0]) / 2
            apx_distance = round( (1-(boxes[0][i][3] - boxes[0][i][1]))**4, 1)
            dragon_dict[apx_distance] = [mid_x, mid_y, scores[0][i]]

if len(dragon_dict) > 0:
    closest = sorted(dragon_dict.keys())[0]
    dragon_choice = dragon_dict[closest]
    determine_movement(mid_x = dragon_choice[0], mid_y = dragon_choice[1]

