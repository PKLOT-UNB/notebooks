import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

df = pd.read_csv("save_ue.csv")


X = []

y = []

for idx, element in enumerate(df.iterrows()):


    img = cv2.imread(element[1]['relative_path'])

    #normalizando as imagens, colocando em um intervalo de 0 a 1

    X.append(img/ 255)
    label = [0, 1] if element[1]['status'] == 'Occupied' else [1, 0]  
    y.append(label)



X_train, X_test = X[0 : int(len(X)*0.75)], X[int(len(X)*0.75): len(X)]
y_train, y_test = y[0 : int(len(y)*0.75)], y[int(len(y)*0.75): len(y)]


X_train, X_test = np.array(X_train), np.array(X_test)
y_train, y_test = np.array(y_train), np.array(y_test)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(176, 93, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2))


model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=10, 
                    validation_data=(X_test, y_test))



