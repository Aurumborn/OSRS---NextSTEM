import numpy as np
import cv2
import time
from directmouse import on_click, check_mouse
from grabscreen import grab_screen                                      # new grab_screen function, its way faster for FPS
from grabkeys import key_check
import os
from pynput import mouse
from pynput.mouse import Button, Controller


def mouse_output(click):                                               #function that one hot encodes the keys for left right and space
    #[Click, x, y]
    output = [0,0,0]
    if click == None:
        pass
    elif True in click[0]:
        output[0] = 1
        output[1] = click[0][1]
        output[2] = click[0][2]    
    return output

file_name = 'training_data.npy'                                         #sets data file name

if os.path.isfile(file_name):                                           #loads file and appends if file is found.
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:                                                                   #if file doesnt exist, creates a new one starting blank
    print('File does not exist, starting fresh')
    training_data = []



def main():                                                             #main function, this is used to create the training data
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    while(True):                                                        #image showing
        if not paused:
            screen = grab_screen(region = (0,30,767, 530))                 #converts image to an array
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)               #converts to grayscale, makes inputs to the neural net easiermain()
            screen = cv2.resize(screen, (76, 53))                           #rezises to simplify the input into the neural net
            click = check_mouse()
            output = mouse_output(click)                                   #one hot encodes the output
            training_data.append([screen, output])                          #appends the data and output to training data

            last_time = time.time()

            if len(training_data) % 100 == 0:                               #prints amount of training data at intervals of 500
                print(len(training_data))
                np.save(file_name, training_data)                           #saves file


        keys = key_check()        
        if 'T' in keys:
            if paused:
                paused = False

                time.sleep(1)
                print('Unpausing')
            else:
                paused = True
                print('Paused')
main()
