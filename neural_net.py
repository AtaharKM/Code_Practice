#Insert Libraries

from time import time
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense, Activation
import datetime
import os

# Insert Database
mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

#prepare database for training and testing
x_train,x_test=x_train/255.0, x_test/255.0

#Define keras model
def create_model():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation="softmax")
    ]
    )

model=create_model()

#Compile Model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#insert callback folder; This structure is important for windows
tensorboard = tf.keras.callbacks.TensorBoard(log_dir=os.path.join(
    "logs",
    "fit",
    datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
))

#Fit the model
model.fit(x_train, y_train, epochs=5,verbose=1, callbacks=[tensorboard])
