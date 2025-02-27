# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:35:27 2019

@author: Prakhar
"""

import os
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras import optimizers


img_width, img_height = 150, 150
train_data_dir = r'C:\Users\Prakhar\Documents\minor project\food processing\test_set'
validation_data_dir = r'C:\Users\Prakhar\Documents\minor project\food processing\training_set'


datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory(train_data_dir, target_size=(img_width, img_height),batch_size=16, class_mode='binary')

validation_generator = datagen.flow_from_directory(validation_data_dir, target_size=(img_width, img_height),batch_size=32,class_mode='binary')

model = Sequential()
model.add(Convolution2D(32, 3, 3, input_shape=(img_width, img_height,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

nb_epoch = 25
nb_train_samples = 2048
nb_validation_samples = 832

model.fit_generator(train_generator, samples_per_epoch=nb_train_samples,nb_epoch=nb_epoch,validation_data=validation_generator,nb_val_samples=nb_validation_samples)

model.save_weights('models/basic_cnn_20_epochs.h5')
#model.load_weights('models_trained/basic_cnn_20_epochs.h5')
model.evaluate_generator(validation_generator, nb_validation_samples)
