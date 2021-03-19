import numpy as np
import cv2
from grabscreen import grab_screen # new grab_screen function, its way faster for FPS
from directmouse import on_click, chec
import time
from grabkeys import key_check
from alexnet import alexnet
import os


WIDTH = 96
HEIGHT = 72                                                                     #sets the starting parameters for height,width, learning rate, and epochs
LR = 1e-3
EPOCHS = 5
MODEL_NAME = 'space_in_{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)   #model name with variables to makae each name unique when things are tweaked





model = alexnet(WIDTH, HEIGHT, LR)                                              #loads the model
model.load(MODEL_NAME)

def main():
    for i in list(range(4))[::-1]:                                              #sleep loop that gives me time to get tabbed over to the game
        print(i+1)
        time.sleep(1)

    last_time = time.time()                                                     #frame timer
    paused = False
    while(True):                                                                #image showing

        if not paused:
            screen = grab_screen(region = (0,40, 960, 720))                     #converts image to an array
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(96, 72))
            
            print('Frame Took {} seconds'.format(time.time()-last_time))        #displays frame time
            last_time = time.time()

            
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]   #creates the predictions based on the model
            moves = list(np.around(prediction))
            print(moves, prediction)

            if moves == [1,0,0]:                                                #if statement checks the preditions and inputs the correct move accordingly
                left()
            elif moves == [0,1,0]:
                right()
            elif moves == [0,0,1]:
                shoot()
            elif moves == [0,0,0]:
                wait()

        keys = key_check()                                                      #checks keys to look for the pause button 'T'

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(D)
                ReleaseKey(space)

        
main()
