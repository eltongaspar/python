
#Aprendizado de máquina 

#Bibliotacas 

import tensorflow as tf
import numpy as np
from tensorflow import keras

#importe uma biblioteca chamada numpy, que representa os dados como listas com facilidade e rapidez.
#O framework para definir uma rede neural como um conjunto de camadas sequenciais é chamado de kera

#Defina e compile a rede neural
#Em seguida, crie a rede neural mais simples possível. Ela tem uma camada, que tem um neurônio, e a forma de entrada dela tem apenas um valor.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


#Em seguida, escreva o código para compilar a rede neural. Ao fazer isso, você precisa especificar duas funções: uma loss e uma optimizer.
model.compile(optimizer='sgd', loss='mean_squared_error')
#A função loss mede as respostas adivinhadas em relação às respostas corretas e avalia o desempenho da qualidade.#
#Em seguida, o modelo usa a função optimizer para fazer outra suposição. Com base na função de perda, ele tenta minimizar a perda. Neste ponto, talvez você veja algo como Y=5X+5. Embora isso ainda seja muito ruim, ele está mais perto do resultado correto (a perda é menor).
#Primeiro, veja como instruí-lo a usar mean_squared_error para a perda e descendente estocástico (sgd) para o otimizador. Você ainda não precisa entender a matemática, mas dá para ver que elas funcionam.

#Fornecer os dados


xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
#Uma biblioteca Python chamada NumPy fornece muitas estruturas de dados de tipo de matriz para fazer isso. Especifique os valores como uma matriz em NumPy com np.array[]


#4. Treinar a rede neural
model.fit(xs, ys, epochs=1)
#O processo de treinamento da rede neural, em que aprende a relação entre X's e Y's, está na chamada model.fit. É a etapa em que ele passará pelo loop antes de tentar adivinhar, medir o desempenho do jogo (da perda) ou usar o otimizador para fazer outra estimativa. Isso acontecerá pelo número de períodos que você especificar. Ao executar esse código, a perda será exibida em cada época.
#Por exemplo, você pode ver que, nas primeiras épocas, o valor da perda é muito grande, mas diminui a cada etapa.
#Conforme o treinamento avança, a perda fica muito pequena em breve.
#No final do treinamento, a perda é extremamente pequena, o que mostra que nosso modelo está fazendo um ótimo trabalho para inferir a relação entre os números.

#5. Use o modelo

#Você tem um modelo treinado para aprender a relação entre X e Y. Você pode usar o método model.predict para descobrir o Y de um X desconhecido anteriormente. Por exemplo, se X for 10, qual você acha que Y será? Tente adivinhar antes de executar este código:
print(model.predict([10.0]))
#As redes neurais lidam com as probabilidades. Por isso, ele calcula que há uma probabilidade muito alta de que a relação entre X e Y seja Y=3X+1, mas não é possível determinar com apenas seis pontos de dados. O resultado é muito próximo de 31, mas não necessariamente de 31.

