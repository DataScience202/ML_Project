# -*- coding: utf-8 -*-
"""M22AI634_Gurmukhi_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tr-I-ipcqL2r4YfCatHT2fSQdbvLw0Tp
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import tensorflow as tf
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline
import os
import cv2

train_path="/content/drive/MyDrive/GurNum-20230416T100840Z-001/GurNum"
val_path="/content/drive/MyDrive/GurNum-20230416T100840Z-001/GurNum"

data_dir = train_path

img_size = (32, 32)
# Create empty lists for the images and labels
images = []
labels = []
# Loop over each folder from '0' to '9'
for label in range(10):
 folder_path = os.path.join(data_dir, 'train', str(label))
 # Loop over each image in the folder
 for file in os.listdir(folder_path):
  file_path = os.path.join(folder_path, file)
  if file_path.endswith(('.tiff','.bmp')):
    # Load the image and resize it to the desired size
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, img_size)
    # Append the image and label to the lists
  images.append(img)
  labels.append(label)

images = np.array(images)
  labels = np.array(labels)
# Save the arrays in NumPy format
  np.save('x_train.npy', images)
  np.save('y_train.npy', labels)
  images = np.array(images)
  labels = np.array(labels)
# Save the arrays in NumPy format
  np.save('x_train.npy', images)
  np.save('y_train.npy', labels)

data_dir_val = val_path
# Set the image size
img_size_val = (32, 32)
# Create empty lists for the images and labels
images_val = []
labels_val = []
# Loop over each folder from '0' to '9'
for label in range(10):
 folder_path = os.path.join(data_dir_val, 'val', str(label))
 # Loop over each image in the folder
 for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if file_path.endswith(('.tiff','.bmp')):
    # Load the image and resize it to the desired size
     img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
     img = cv2.resize(img, img_size_val)
     # Append the image and label to the lists
 images_val.append(img)
 labels_val.append(label)

images_val = np.array(images_val)
labels_val = np.array(labels_val)

np.save('x_test.npy', images_val)
np.save('y_test.npy', labels_val)

# Load the dataset
x_train = np.load('x_train.npy')
y_train = np.load('y_train.npy')
x_test = np.load('x_test.npy')
y_test = np.load('y_test.npy')

print(len(x_train))
print(len(x_test))
x_train[0].shape
x_train[0]
plt.matshow(x_train[0])
plt.matshow(x_train[9])
print(x_train.shape)
print(x_test.shape)
y_train
y_test
plt.matshow(x_test[9])

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(32,32)))
model.add(tf.keras.layers.Dense(units=1024, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=1024, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=1024, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train,epochs= 100, validation_data=(x_test, y_test))

x_train_scaled = x_train/255
x_test_scaled = x_test/255
model.fit(x_train_scaled, y_train,epochs= 10, validation_data=(x_test_scaled, y_test))

model.evaluate(x_test_scaled,y_test)

plt.matshow(x_test[0])
y_predicted = model.predict(x_test_scaled)
y_predicted[0]
# this showing the 10 results for the input '0', we need to look for the value which is max
print('Predicted Value is ',np.argmax(y_predicted[0]))

plt.matshow(x_test[7])
print('Predicted Value is ',np.argmax(y_predicted[7]))

loss,accuracy =model.evaluate(x_test_scaled,y_test)
print(loss)
print(accuracy)