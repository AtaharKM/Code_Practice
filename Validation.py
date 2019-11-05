from __future__ import print_function
import math
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf

from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)

pd.options.display.max_rows=10
pd.options.display.float_format='{:.1f}'.format

california_housing_dataframe=pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv",sep=',')

california_housing_dataframe=california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))

def preprocess_features(california_housing_dataframe):

    selected_features=california_housing_dataframe[["latitude",'longitude','housing_median_age','total_rooms', 'total_bedrooms','population','households',
                                                    'median_income']]
    processed_features=selected_features.copy()

    processed_features['rooms_per_person']=california_housing_dataframe['total_rooms']/california_housing_dataframe['population']

    return processed_features

def preprocess_targets(california_housing_dataframe):
    output_targets=pd.DataFrame()
    output_targets['median_house_value']=(california_housing_dataframe['median_house_value']/1000.0)

    return output_targets

training_examples=preprocess_features(california_housing_dataframe.head(12000))
training_examples.describe()

training_targets=preprocess_targets(california_housing_dataframe.head(12000))
training_targets.describe()

validation_examples=preprocess_features(california_housing_dataframe.tail(5000))
validation_examples.describe()

validation_target=preprocess_targets(california_housing_dataframe.tail(5000))
validation_target.describe()

correlation_dataframe=training_examples.copy()
correlation_dataframe['target']=training_targets['median_house_value']

t=correlation_dataframe.corr()