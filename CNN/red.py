import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import scipy.io as sio
import numpy as np
from sklearn.utils import shuffle
from scipy.io import loadmat

#physical_devices = tf.config.list_physical_devices("GPU")
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

mat_contents = sio.loadmat('dataSet.mat')

X_train=mat_contents['X_train']
X_train=X_train.reshape((X_train.shape[0],1,X_train.shape[1]))
print(X_train.shape)
X_test=mat_contents['X_test']
X_test=X_test.reshape((X_test.shape[0],1,X_test.shape[1]))
print(X_train.shape)
X_val=mat_contents['X_val']
X_val=X_val.reshape((X_val.shape[0],1,X_val.shape[1]))

Y_train=tf.keras.utils.to_categorical(mat_contents['Y_train'].T)
Y_test=tf.keras.utils.to_categorical(mat_contents['Y_test'].T)
Y_val=tf.keras.utils.to_categorical(mat_contents['Y_val'].T)

def resblock(x, kernelsize, filters):
    fx = layers.Conv2D(filters, kernelsize, activation='relu', padding='same')(x)
    fx = layers.BatchNormalization()(fx)
    fx = layers.Conv2D(filters, kernelsize, padding='same')(fx)
    out = layers.Add()([x,fx])
    out = layers.ReLU()(out)
    out = layers.BatchNormalization()(out)
    return out

def No_Residual():
    inputs = keras.Input(shape=(1,640))
    x=layers.Conv1D(64,5,activation='relu',padding='same')(inputs)
    x=layers.MaxPool1D(8,padding="same")(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.MaxPool1D(8,padding="same")(x)
    x=layers.Flatten()(x)
    x=layers.Dense(64,activation='relu')(x)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(5,activation='softmax')(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model

def Residual():
    inputs = keras.Input(shape=(1,640))
    x=layers.Conv1D(16,5,padding='same',activation='relu')(inputs)
    x=layers.Conv1D(16,5,padding='same',activation='relu')(x)
    x=layers.Conv1D(16,5,padding='same',activation='relu')(x)
    x=layers.Conv1D(640,5,padding='same',activation='relu')(x)
    x=layers.add([inputs,x])
    x=layers.Conv1D(64,5,activation='relu',padding='same')(x)
    x=layers.MaxPool1D(8,padding="same")(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.Conv1D(32,5,activation='relu',padding='same')(x)
    x=layers.MaxPool1D(8,padding="same")(x)
    x=layers.Flatten()(x)
    x=layers.Dense(64,activation='relu')(x)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(5,activation='softmax')(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model
    
model = No_Residual()
model.compile(
        loss=keras.losses.CategoricalCrossentropy(),
        optimizer=keras.optimizers.Adam(lr=1e-3),
        metrics=["categorical_accuracy"],
        )

model.summary()

model.fit(X_train,Y_train,validation_data=(X_val,Y_val), batch_size=256, epochs=300, verbose=1)