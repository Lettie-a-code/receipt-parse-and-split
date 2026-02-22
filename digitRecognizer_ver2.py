# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 17:51:21 2025

@author: Elizabeth
Simple CNN for MNIST Digit Classification
1.  Downloads MNIST
2.  Preprocesses the images.
3.  Builds a CNN with 2 convolution layers + 2 pooling layers.
4.  Trains the network.
5.  Prints the accuracy each epoch.
6.  Evaluates o the test sign
"""

# A program that uses CNN for MNIST Digit Classification
# Step 1: Import all required keras libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Step 2: Load and return training and test datasets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Original Dataset Shapes:")
print("x_train:", x_train.shape)
print("y_train:", y_train.shape)
print("x_test:", x_test.shape)
print("y_test:", y_test.shape)

# ------------------------------------------------------
# Step 3: define your CNN model 

# MNIST images are 28x28 grayscale; CNN expects (28,28,1)
x_train = x_train.reshape((-1, 28, 28, 1)).astype("float32") / 255.0
x_test = x_test.reshape((-1, 28, 28, 1)).astype("float32") / 255.0

# ------------------------------------------------------
# Step 4: Call digit_recognition_cnn() to build your model (2 conv + 2 pooling layers)
# 3. Build CNN Model 
model = models.Sequential()

# 1st Convolution + Pooling
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# 2nd Convolution + Pooling
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten for fully connected layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# Output layer — 10 classes (digits 0–9)
model.add(layers.Dense(10, activation='softmax'))

# ------------------------------------------------------
# Step 5: Train your model and see the result in Command window. Set epochs to a number between 10 - 20 and batch_size between 150 - 200

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ------------------------------------------------------
# 5. Train CNN

history = model.fit(
    x_train, y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    batch_size=64
)

# ------------------------------------------------------
# 6. Evaluate on Test Data

test_loss, test_acc = model.evaluate(x_test, y_test)
print("\nFinal Test Accuracy:", test_acc)

# Save the trained model
model.save('digitRecognizer.h5')
print("Model saved as digitRecognizer.h5")

