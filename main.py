
import numpy as np
import cv2
from grabscreen import grab_screen
from directkeys import ReleaseKey, PressKey, W, A, S, D
import time
from grabkeys import key_check
import os
from pynput import mouse
from pynput.mouse import Button, Controller

m = Controller()



def roi(img, vertices):                                                         #defines the ROI
    mask = np.zeros_like(img)                                                           
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

#process image function
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)            #converts to grayscale, makes inputs to the neural net easier
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2 = 300)  #canny edge detection looks for edges
    vertices = np.array([[0,30],[767,30],[767,530], [0,530]])             #assigns vertices for the roi
    processed_img = roi(processed_img, [vertices])                              #processed img is now the roi
    return processed_img





def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()

    while(True):                                                                    #image showing
        screen = grab_screen(region = (0,40, 767, 530))                  #converts image to an array
        print('Frame Took {} seconds'.format(time.time()-last_time))


        last_time = time.time()

        new_screen = process_img(screen)           #returns a processed image to the new_screen variable
        cv2.imshow('window', new_screen)                                #shows the image
       
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
