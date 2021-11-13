import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from tensorflow.keras import metrics
from tensorflow.keras import optimizers
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, LabelEncoder

import csv 
import pandas as pd
import random
import matplotlib.pyplot as plt

seed = 7
numpy.random.seed(seed)


def rand_index(limit):
    number = 0
    index_list = list(range(limit))
    random.shuffle(index_list)
    return index_list
def select_variables(stars,types,index_list,number_train):
    #0:6
    #stars.iloc[filas: indices[0->number_rows_for_train] , columnas ]
    x_train = stars.iloc[index_list[0:number_train],:]
    x_test = stars.iloc[index_list[number_train:],:]
    
    y_train = types.iloc[index_list[:number_train]]
    y_test =  types.iloc[index_list[number_train:]]
    return x_train, y_train, x_test, y_test
def convert(list_train):
    y = []
    ls = []
    for i in list_train:
        ls = [0 for i in range(6)]
        ls[i] = 1
        y.append(ls)
    return pd.DataFrame(y)
def IntegerEncode2(target):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(target)
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    target = pd.DataFrame(onehot_encoded)
    return target


def index_list(colors, color):
    i = colors.index(color)
    return i 

def add_values(stars,index,list_values,lower=False):
    values = [0 for _ in range(len(list_values))]
    mat_values = []
    for row in stars.values:
        values_row = values.copy()
        value = row[index]
        if (lower):
            value = value.lower()
        values_row[index_list(list_values,value)] = 1
        mat_values.append(values_row)
    return mat_values


def convert_categoricals(stars,colors, spectral_classes):
    
    mat_values = add_values(stars,4,colors,True)
    categories_colors = pd.DataFrame(mat_values,columns=colors)
    
    mat_values = add_values(stars,5,spectral_classes)
    categories_spectral_classes = pd.DataFrame(mat_values,columns=spectral_classes)
    
    return pd.concat([categories_colors, categories_spectral_classes],axis=1)

def printv():
    print("aqui aaaa")
def get_inputs(stars,colors, spectral_classes):
    return pd.concat([stars.iloc[:,0:4],convert_categoricals(stars,colors, spectral_classes)],axis=1)


def convert_at_type_array(mat):
    types = []
    for row in mat:
        value = 0
        for index in row:
            if (index >= 1):
                break
            value += 1
        types.append(value)
    return types

def stadistics(y_real, y_predicted):
    counter = 0
    total = len(y_real)
    for i in range(total):
        if (y_real[i] == y_predicted[i]):
            counter += 1
    print(f"Cantidad total de pruebas: {total}")
    print(f"Cantidad total de aciertos: {counter}")
    print(f"Porcentaje de aciertos: {counter/total*100}%")