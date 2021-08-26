import tensorflow as tf
import numpy as np 
from tensorflow import keras
from matplotlib import pyplot as plt
import cv2
import sys

def CNN():
	(x_tr, y_tr), (x_ts, y_ts) = keras.datasets.mnist.load_data()
	x_tr = x_tr /255
	x_ts = x_ts /255
	x_flatten_tr = x_tr.reshape(len(x_tr), 784)
	x_flatten_ts = x_ts.reshape(len(x_ts), 784)
	#print(x_flatten_ts.shape)
	model = keras.Sequential(
		keras.layers.Dense(10, input_shape = (784,), activation = "sigmoid")
	)
	model.compile(
	    optimizer = "adam",
	    loss = 'sparse_categorical_crossentropy',
	    metrics = ['accuracy']
	)
	model.fit(x_flatten_tr, y_tr, epochs = 20)
	model.evaluate(x_flatten_ts, y_ts)
	y = model.predict(x_flatten_ts)
	return model

print(prediction("data_img/number(1).png"))
CNN()