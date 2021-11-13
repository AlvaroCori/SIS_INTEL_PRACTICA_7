# SIS_INTEL_PRACTICA_7
Neural networks for classification of stars


#### Experiment 1 
index_list = rand_index(stars.shape[0])

x_train, y_train, x_test, y_test = select_variables(stars,index_list, 190)
x_test
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

y = []
ls = []

for i in y_train:
    ls = [0 for i in range(6)]
    ls[i] = 1
    y.append(ls)
y = pd.DataFrame(y)

model.fit(x_train, y, epochs=1000)


scores = model.evaluate(x_train, y)
 
    
y_t = []
ls = []
for i in y_test:
    ls = [0 for i in range(6)]
    ls[i] = 1
    y_t.append(ls)
y_t = pd.DataFrame(y_t)

print (model.predict(x_test).round())
print (y_t)


#### Experiment 2
x_train, y_train, x_test, y_test = select_variables(stars,index_list, 160)
model = Sequential()
model.add(Dense(10, input_dim=4, activation='selu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Epoch 1000/1000
5/5 [==============================] - 0s 5ms/step - loss: 0.2177 - accuracy: 0.9750

#### Experiment 3

This experiment use 
x_train, y_train, x_test, y_test = select_variables(stars_inputs,types,index_list, 160)
model = Sequential()
model.add(Dense(10, input_dim=24, activation='selu'))
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

Epoch 1482/1482
3/3 [==============================] - 0s 31ms/step - loss: 1.6489 - accuracy: 0.9688 - val_loss: 0.0665 - val_accuracy: 1.0000

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