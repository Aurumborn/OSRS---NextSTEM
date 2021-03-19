import numpy as np
import cv2
import time
from directmouse import on_click, check_mouse
from grabscreen import grab_screen                                      # new grab_screen function, its way faster for FPS
from grabkeys import key_check
import os
from pynput import mouse
from pynput.mouse import Button, Controller


def roi(img, vertices):                                                         #defines the ROI
    mask = np.zeros_like(img)                                                           
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_health(image):                  #process health, takes screen and returns % of current enemies health
    health_roi = np.array([[20,88],[20,72],[140,72],[140,88]])

    #image = roi(image, [health_roi])

    #damage = (99,12,17)
    #damage_upper = (102,21,23)

    damage_value = [99,20,19]               #pixel color value for damage
    health_value = [7,138,54]               #pixel color value for health

    

    
    #health_left = (5,135,50)
    #health_left_upper = (8,141,57)
    
    damage_result = np.count_nonzero(np.all(image==damage_value,axis=2))        #find damage pixels
    health_result = np.count_nonzero(np.all(image==health_value,axis=2))        #find health pixels




    

    
    total_health = damage_result + health_result                                #calcs % of health
    if total_health != 0:
        enemy_health = (health_result/total_health) * 100
        return enemy_health
    else:
        return 0    
    
def process_player_health(image):                                               #same thing as before but for player health
    player_roi = np.array([[250,200],[250,190],[280,190],[280,190]])
    player_damage = [255,0,0]
    player_health = [0,255,0]

    player_damage_result = np.count_nonzero(np.all(image==player_damage,axis=2))
    player_health_result = np.count_nonzero(np.all(image==player_health,axis=2))

    player_total_health = player_damage_result + player_health_result
    if player_total_health != 0:
        player_health = (player_health_result/player_total_health) * 100
        return player_health
    else:
        return 0  


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()

    while(True):                                                                    #image showing
        screen = grab_screen(region = (0,40, 767, 530))                  #converts image to an array
        enemy_health = process_health(screen)
        player_health = process_player_health(screen)
        print('Player Health:', player_health)
        print("Enemy Health:", enemy_health)
        print('Frame Took {} seconds'.format(time.time()-last_time))


        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
