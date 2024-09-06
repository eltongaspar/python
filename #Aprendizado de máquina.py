# Aprendizado de máquina

# Bibliotecas
import tensorflow as tf
import numpy as np
from tensorflow import keras

# Defina e compile a rede neural
# Crie a rede neural mais simples possível. Ela tem uma camada, que tem um neurônio, e a forma de entrada dela tem apenas um valor.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Compilar a rede neural especificando a função loss e o optimizer.
model.compile(optimizer='sgd', loss='mean_squared_error')

# Fornecer os dados
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Treinar a rede neural
model.fit(xs, ys, epochs=1)  # Treine por mais épocas para um ajuste melhor

# Use o modelo
# Faça uma predição com o modelo treinado
input_data = np.array([10.0])  # Converta a lista para um array NumPy
print(model.predict(input_data))
