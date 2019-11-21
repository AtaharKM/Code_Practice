#Insert Libraries

from time import time
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense, Activation
import datetime
import os
import tarfile
from six.moves import urllib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


DOWNLOAD_ROOT="https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH=os.path.join('datasets', 'housing')
HOUSING_URL=DOWNLOAD_ROOT+'datasets/housing/housing.tgz'

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path=os.path.join(housing_path,"housing.tgz")
    urllib.request.urlretrieve(housing_url,tgz_path)
    housing_tgz=tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path=os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    shuffled_indices=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_indices=shuffled_indices[:test_set_size]
    train_indices=shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
from zlib import crc32
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier))&0xffffffff< test_ratio*2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids=data[id_column]
    in_test_set=ids.apply(lambda id_:test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


data=load_housing_data(HOUSING_PATH)
train_set, test_set=split_train_test(data,0.2)

housing_with_id=data.reset_index()

train_set,test_set=split_train_test_by_id(housing_with_id,0.2,'index')

train_set,test_set=train_test_split(data, test_size=0.2, random_state=42)







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
