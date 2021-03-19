import numpy as np
from alexnet import alexnet                     #import alex net
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization



WIDTH = 76
HEIGHT = 53                 #sets the starting parameters for height,width, learning rate, and epochs
LR = 1e-3
EPOCHS = 3
MODEL_NAME = 'osrs{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)           #model name with variables to makae each name unique when things are tweaked

model = alexnet(WIDTH, HEIGHT, LR)              #initializes the net to model

train_data = np.load('training_data_v2.npy', allow_pickle = True)           #sets allow pickle to true when loading data set

train = train_data[:-4000]           #separates the train and test data sets
test = train_data[-4000:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)                   #assigns the X and Y for fitting
Y = [i[1] for i in train]

test_X = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)               #assigns the test X and Test Y
test_Y = [i[1] for i in test]
#fits the model
model.fit({'input': X}, {'targets': Y}, n_epoch = EPOCHS,
          validation_set = ({'input': test_X}, {'targets': test_Y}),
          snapshot_step = 75, show_metric = True, run_id=MODEL_NAME)
#saves model name
model.save(MODEL_NAME)
