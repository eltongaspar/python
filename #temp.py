#Temp 


#Aprendizado com redes neurais
# Importando as bibliotecas
import cv2
import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Carregar as imagens e seus respectivos IDs
def getImagemComId():
    dir = 'D:/Dados/Material_complementar_reconhecimento_facial/capturas'
    caminhos = [os.path.join(dir, f) for f in os.listdir(dir)]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

# Carregar os dados
ids, faces = getImagemComId()

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(faces, ids, test_size=0.2, random_state=42)

# Pré-processamento dos dados
input_shape = (200, 200)  # dimensão da imagem
X_train = np.array([cv2.resize(img, input_shape) for img in X_train])
X_test = np.array([cv2.resize(img, input_shape) for img in X_test])

# Normalização dos dados
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Definir a arquitetura da rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=input_shape),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
print("Treinando...")
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test)
print("Accuracy:", accuracy)

# Salvar o modelo
model.save('D:/Dados/Material_complementar_reconhecimento_facial/cascades/modelo_rede_neural.h5')
print("Modelo salvo com sucesso!")
