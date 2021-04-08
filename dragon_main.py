import numpy as np
import cv2
import time
from directmouse import on_click, check_mouse
from grabscreen import grab_screen                                      # new grab_screen function, its way faster for FPS
from grabkeys import key_check
import os
from pynput import mouse
from pynput.mouse import Button, Controller
import torch
from detecto import core,utils,visualize


def roi(img, vertices):                                                         #defines the ROI
    mask = np.zeros_like(img)                                                           
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_health(image):                  #process health, takes screen and returns % of current enemies health
    health_roi = np.array([[20,88],[20,72],[140,72],[140,88]])

    #image = roi(image, [health_roi])

    damage_value = [99,20,19]               #pixel color value for damage
    health_value = [7,138,54]               #pixel color value for health
    
    damage_result = np.count_nonzero(np.all(image==damage_value,axis=2))        #find damage pixels
    health_result = np.count_nonzero(np.all(image==health_value,axis=2))        #find health pixels

    total_health = damage_result + health_result                                #calcs % of health
    if total_health != 0:
        enemy_health = (health_result/total_health) * 100
        return enemy_health
    else:
        return 0    
    
def process_player_health(image):                                               #same thing as before but for player health
    #player_roi = np.array([[250,200],[250,190],[280,190],[280,200]])
    player_roi = np.array([[535,487],[535,237],[550,237],[550,487]])
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

model = core.Model.load('model_weights.pth', ['dragon'])
#if torch.cuda.is_available():
#    print('Switching to GPU')
#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#model = model.to(device)


def detect_dragons():
    dragon_screen = grab_screen(region = (0,30, 520, 365))
    
    predictions = model.predict(dragon_screen)

    labels, boxes, scores = predictions

    new_scores = []
    new_boxes = []
    i = 0
    for score in scores:
        if score >= 0.91:
            new_scores.append(score)
            new_boxes.append(boxes[i])
        i += 1
    return new_scores, new_boxes


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()

    while(True):                                                                    #image showing
        screen = grab_screen(region = (0,30, 767, 530))                  #converts image to an array
        enemy_health = process_health(screen)
        player_health = process_player_health(screen)

        if enemy_health <= 30:
            dragon_probs, dragon_locs = detect_dragons()
            print('Dragons: ', dragon_probs)
        print('Player Health: ', round(player_health,2), "Enemy Health: ", round(enemy_health,2))
        print('Frame Took {} seconds'.format(time.time()-last_time))


        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
