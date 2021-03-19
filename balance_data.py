#balance data is used to balance the dataset to avoid over-learning

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('training_data.npy', allow_pickle=True)        #imports train data
print(len(train_data))
df = pd.DataFrame(train_data)
print(Counter(df[1].apply(str)))                                    #prints the counts of the different inputs

### clear invent bounds are (x [443, 477] y [322, 356])

trees = []
bank = []
clear_inventory = []
moves = []

shuffle(train_data)

emp = [0,0,0]
for data in train_data:
    img = data[0]
    choice = data[1]

    if choice != emp:
        if choice[1] <= 260: 
            bank.append([img, choice])
        elif choice[1] in range(443, 477) and choice[2] in range(332, 356):
            clear_inventory.append([img, choice])
        else:
            if choice[1] in range(1, 767) and choice[2] in range(30, 530):
                trees.append([img, choice])
    elif choice == emp:
        moves.append([img, choice])
    else:
        print('no matches@@@@@@@')




final_data = trees + bank + clear_inventory

shuffle(final_data)

print(len(final_data))
print("trees:")
print(len(trees))
print("bank:")
print(len(bank))
print("clear_inventory:")
print(len(clear_inventory))
print('Moves: {}'.format(len(moves)))
np.save('training_data_v2.npy', final_data)


##for data in train_data:                                         #loop displays the choice and game image for each frame
##    img = data[0]
##    choice = data[1]
##    cv2.imshow('test', img)
##    print(choice)
##    if cv2.waitKey(25) & 0xFF == ord('q'):
##        cv2.destroyAllwindows()
##        break
