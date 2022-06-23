# -*- coding: utf-8 -*-
"""Handwritten Digit Recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFPdAaFC5L9SCx3bXL5MRkSaHXtfXFPN
"""

#import the following libraries and data set
import tensorflow
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Dropout
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras import backend as K

#to split the data of training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#dimension of the training data
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)
#convert class vectors to binary class matrices
num_classes = 10
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#create a training model
batch_size = 128
epochs = 10
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape = input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=tensorflow.keras.optimizers.Adadelta(),metrics=['accuracy'])

#train the model
hist = model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(x_test, y_test))
print("The model has successfully trained")
model.save('mnist.h5')
print("Saving the bot as mnist.h5")

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img('num_2_1.png', grayscale=True, target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

# make a prediction for a new image.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import argmax
from keras.models import load_model

#display image wanted to be tested
print("The image wanted to be tested: ")
image = mpimg.imread('num_2_1.png')
imgplot = plt.imshow(image)
plt.show()

# load an image and predict the class
def run_example():
	# load the image
	img = load_image('num_2_1.png')
	# load model
	model = load_model('mnist.h5')
	# predict the class
	predict_value = model.predict(img)
	digit = argmax(predict_value)
	print(digit)
 
# entry point, run the example
run_example()