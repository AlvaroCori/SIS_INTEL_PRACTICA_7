# SIS_INTEL_PRACTICA_7
Neural networks for classification of stars


Experiment 1 
index_list = rand_index(stars.shape[0])

x_train, y_train, x_test, y_test = select_variables(stars,index_list, 190)
x_test
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

y = []
ls = []
'''
[0,1,2,3,4,5]
[
[1,0,0,0,0,0]
[0,1,0,0,0,0]
[0,0,1,0,0,0]
[0,0,0,1,0,0]
[0,0,0,0,1,0]
[0,0,0,0,0,1]
]
'''
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


Experiment 2
x_train, y_train, x_test, y_test = select_variables(stars,index_list, 160)
model = Sequential()
model.add(Dense(10, input_dim=4, activation='selu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Epoch 1000/1000
5/5 [==============================] - 0s 5ms/step - loss: 0.2177 - accuracy: 0.9750