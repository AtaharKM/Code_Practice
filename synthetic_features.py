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

california_housing_dataframe["median_house_value"]/=1000.0

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):

    features={key: np.array(value) for key,value in dict(features).items()}

    ds=Dataset.from_tensor_slices((features,targets))
    ds=ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds=ds.shuffle(buffer_size=10000)
    features, labels=ds.make_one_shot_iterator().get_next()

    return features, labels

def train_model(learning_rate, steps, batch_size, input_features):
    period=10
    steps_per_period=steps/period
    my_feature=input_features
    my_feature_data=california_housing_dataframe[[my_feature]].astype('float32')
    my_label='median_house_value'
    targets=california_housing_dataframe[my_label].astype('float32')

    training_input_fn=lambda : my_input_fn(my_feature_data,targets, batch_size=batch_size)
    predict_training_input_fn=lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)

    feature_columns=[tf.feature_column.numeric_column(my_feature)]

    my_optimizer=tf.train.ProximalGradientDescentOptimizer(learning_rate=learning_rate)

    my_optimizer=tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

    linear_regressor=tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)

    plt.figure(figsize=(15,6))
    plt.subplot(1,2,1)
    plt.title("Learned Line by Period")
    plt.ylabel(my_label)
    plt.xlabel(my_feature)

    sample=california_housing_dataframe.sample(n=300)

    plt.scatter(sample[my_feature],sample[my_label])
    colors=[cm.coolwarm(x) for x in np.linspace(-1,1,period)]

    print("Training model....")
    print("RMSE (on training data):")

    root_mean_squared_errors=[]

    for periods in range(0, period):
        linear_regressor.train(input_fn=training_input_fn,steps=steps_per_period,)

        predictions=linear_regressor.predict(input_fn=predict_training_input_fn)
        predictions=np.array([item['predictions'][0] for item in predictions])

        root_mean_squared_error=math.sqrt(metrics.mean_squared_error(predictions,targets))
        print("period %02d:%0.2f"%(periods, root_mean_squared_error))
        root_mean_squared_errors.append(root_mean_squared_error)
        y_extents=np.array([0,sample[my_label].max()])
        weight=linear_regressor.get_variable_value('linear/linear_model/%s/weights'%input_features)[0]
        bias=linear_regressor.get_variable_value('linear/linear_model/bias_weights')

        x_extents=(y_extents-bias)/weight
        x_extents=np.maximum(np.minimum(x_extents,sample[my_feature].max()), sample[my_feature].min())

        # y_extents=(y_extents-bias)/weight
        # x_extents=np.maximum(np.minimum(x_extents,sample[my_feature].max()),sample[my_feature].min())

        y_extents=weight*x_extents+bias
        plt.plot(x_extents, y_extents, color=colors[periods])
    print("Model Training Finished")

    plt.subplot(1,2,2)
    plt.ylabel('RMSE')
    plt.xlabel('Periods')
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(root_mean_squared_errors)

    calibration_data=pd.DataFrame()
    calibration_data["predictions"]=pd.Series(predictions)
    calibration_data["targets"]=pd.Series(targets)
    display.display(calibration_data.describe())

    print("Final RMSE (on training data): %0.2f"%root_mean_squared_error)

    return calibration_data

california_housing_dataframe['rooms_per_person']=california_housing_dataframe['total_rooms']/california_housing_dataframe['population']

calibration_data=train_model(learning_rate=0.05, steps=500, batch_size=5, input_features='rooms_per_person')

plt.figure()
plt.subplot(1,2,1)
plt.scatter(calibration_data["predictions"],calibration_data["targets"])

plt.subplot(1,2,2)
_=california_housing_dataframe['rooms_per_person'].hist()

clipped_features=california_housing_dataframe["rooms_per_person"].apply(lambda x: min(x,3.6))

plt.figure()
h=clipped_features.hist()
california_housing_dataframe['rooms_per_person_clipped']=clipped_features

calibration_data=train_model(learning_rate=0.05, steps=500, batch_size=5, input_features='rooms_per_person_clipped')

plt.figure()
plt.subplot(1,2,1)
plt.scatter(calibration_data["predictions"],calibration_data["targets"])