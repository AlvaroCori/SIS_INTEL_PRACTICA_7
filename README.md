# SIS_INTEL_PRACTICA_7

## Por:
#### Alvaro Bryan Cori Sanchez
#### Mauricio Balderrama Ali

Neural networks for classification of stars


#### Experiment 1

190 -> train
 10 -> test 

model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Epoch 900/900
3/3 [==============================] - 0s 38ms/step - loss: 4.6404 - accuracy: 0.7421 - val_loss: 0.1054 - val_accuracy: 0.9000

Cantidad total de pruebas: 10
Cantidad total de aciertos: 9
Porcentaje de aciertos: 90.0%


#### Experiment 2

160 -> train
 40 -> test 
 
model = Sequential()
model.add(Dense(10, input_dim=4, activation='selu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Epoch 1000/1000
5/5 [==============================] - 0s 5ms/step - loss: 0.2177 - accuracy: 0.9750

Cantidad total de pruebas: 40
Cantidad total de aciertos: 40
Porcentaje de aciertos: 100.0%

#### Experiment 3

160 -> train
 40 -> test 


model.add(Dense(10, input_dim=24, activation='selu'))
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])


Epoch 1482/1482
3/3 [==============================] - 0s 31ms/step - loss: 1.6489 - accuracy: 0.9688 - val_loss: 0.0665 - val_accuracy: 1.0000


#### Experiment 4

160 -> train
 40 -> test 
 
model.add(Dense(10, input_dim=24, activation='elu'))
model.add(Dense(6, activation='softmax'))

Cantidad total de pruebas: 40
Cantidad total de aciertos: 40
Porcentaje de aciertos: 100.00%

Epoch 2000/2000
3/3 [==============================] - 0s 29ms/step - loss: 1.4569 - accuracy: 0.9625 - val_loss: 2.1046 - val_accuracy: 0.9750

#### Experiment 5

160 -> train
 40 -> test 

model.add(Dense(64, input_dim=24, activation='selu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

Cantidad total de pruebas: 40
Cantidad total de aciertos: 39
Porcentaje de aciertos: 97.5%

Epoch 4000/4000
3/3 [==============================] - 0s 17ms/step - loss: 0.6752 - accuracy: 0.9563 - val_loss: 3.7892 - val_accuracy: 0.9750


### Bibliografy
#### Open a CSV
https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
#### Save in a dataframe pandas
https://realpython.com/pandas-python-explore-dataset/
#### Aleatory values for a list 
ttps://www.iteramos.com/pregunta/17907/la-mejor-manera-de-aleatorizar-una-lista-de-cuerdas-en-python

#### excel
https://gonzalezgouveia.com/como-exportar-data-frames-de-pandas-a-csv-o-excel-en-python/
https://www.delftstack.com/es/howto/python-pandas/pandas-remove-index/#:~:text=Si%20queremos%20eliminar%20la%20columna,en%20el%20m%C3%A9todo%20reset_index()%20
#### dataframe  
https://www.codigopiton.com/como-crear-un-dataframe-con-pandas-y-python/
#### concatenar dataframes
https://www.analyticslane.com/2018/09/10/unir-y-combinar-dataframes-con-pandas-en-python/