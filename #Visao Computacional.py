#Visao Computacional 

#Além do Hello World, um exemplo de visão computacional
#No exercício anterior você viu como criar uma rede neural que descobrisse o problema que você estava tentando resolver. Isso deu um exemplo explícito de comportamento aprendido. É claro que, nesse caso, foi um pouco exagerado porque teria sido mais fácil escrever a função Y=3x+1 diretamente, em vez de se preocupar em usar o aprendizado de máquina para aprender a relação entre X e Y para um conjunto fixo de valores e estendendo isso para todos os valores.
#Mas e um cenário em que escrever regras como essa seja muito mais difícil – por exemplo, um problema de visão computacional? Vamos dar uma olhada em um cenário onde podemos reconhecer diferentes peças de roupa, treinadas a partir de um conjunto de dados contendo 10 tipos diferentes.

#Iniciando o código
#Vamos começar com nossa importação do TensorFlow

import tensorflow as tf
print(tf.__version__)

#Treinaremos uma rede neural para reconhecer peças de roupa de um conjunto de dados comum chamado Fashion MNIST. Você pode aprender mais sobre este conjunto de dados aqui.
#Contém 70.000 peças de roupa em 10 categorias diferentes. Cada peça de roupa está em uma imagem em escala de cinza 28x28. Você pode ver alguns exemplos aqui:

#Os dados do Fashion MNIST estão disponíveis diretamente na API de conjuntos de dados tf.keras. Você carrega assim:
mnist = tf.keras.datasets.fashion_mnist

#Chamar load_data neste objeto fornecerá dois conjuntos de duas listas, estes serão os valores de treinamento e teste para os gráficos que contêm os itens de vestuário e suas etiquetas.
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

#Como são esses valores? Vamos imprimir uma imagem de treinamento e um rótulo de treinamento para ver... Experimente diferentes índices no array. Por exemplo, dê uma olhada também no índice 42...é uma inicialização diferente daquela no índice 0
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

#Você notará que todos os valores do número estão entre 0 e 255. Se estivermos treinando uma rede neural, por vários motivos, será mais fácil tratar todos os valores como entre 0 e 1, um processo chamado 'normalização'. .e felizmente em Python é fácil normalizar uma lista como essa sem fazer loop. Você faz assim:
training_images  = training_images / 255.0
test_images = test_images / 255.0

#Agora você deve estar se perguntando por que existem 2 conjuntos... treinamento e teste - lembra que falamos sobre isso na introdução? A ideia é ter 1 conjunto de dados para treinamento e depois outro conjunto de dados... que o modelo ainda não viu... para ver quão bom seria na classificação de valores. Afinal, quando terminar, você vai querer experimentar com dados que ainda não tinha visto!

#Vamos agora projetar o modelo. Existem alguns conceitos novos aqui, mas não se preocupe, você vai pegar o jeito.
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(1024, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(100, activation=tf.nn.softmax)])


#Sequencial: Isso define uma SEQUÊNCIA de camadas na rede neural
#Flatten: Lembra antes onde nossas imagens eram quadradas, quando você as imprimiu? Flatten apenas pega esse quadrado e o transforma em um conjunto unidimensional.
#Denso: Adiciona uma camada de neurônios
#Cada camada de neurônios precisa de uma função de ativação que lhes diga o que fazer. Há muitas opções, mas use-as por enquanto.
#Relu efetivamente significa "Se X> 0 retornar X, caso contrário, retornar 0" - então, o que ele faz é passar apenas valores 0 ou maiores para a próxima camada da rede.
#Softmax pega um conjunto de valores e efetivamente escolhe o maior deles, então, por exemplo, se a saída da última camada for semelhante a [0,1, 0,1, 0,05, 0,1, 9,5, 0,1, 0,05, 0,05, 0,05], ele salva você pesca nele em busca do maior valor e o transforma em [0,0,0,0,1,0,0,0,0] - O objetivo é economizar muita codificação!

#A próxima coisa a fazer, agora que o modelo está definido, é realmente construí-lo. Você faz isso compilando-o com um otimizador e uma função de perda como antes - e então você o treina chamando *model.fit * pedindo para ajustar seus dados de treinamento aos seus rótulos de treinamento - ou seja, faça com que ele descubra a relação entre o dados de treinamento e seus rótulos reais; portanto, no futuro, se você tiver dados semelhantes aos dados de treinamento, ele poderá fazer uma previsão de como seriam esses dados.
model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=100)

#Depois de concluir o treinamento - você deverá ver um valor de precisão no final da época final. Pode parecer algo como 0,9098. Isso indica que sua rede neural tem cerca de 91% de precisão na classificação dos dados de treinamento. Ou seja, descobriu uma correspondência de padrão entre a imagem e os rótulos que funcionou 91% das vezes. Não é ótimo, mas não é ruim, considerando que foi treinado apenas por 5 épocas e feito rapidamente.
#Mas como isso funcionaria com dados invisíveis? É por isso que temos as imagens de teste. Podemos chamar model.evaluate e passar os dois conjuntos, e ele reportará a perda de cada um. Vamos tentar:
model.evaluate(test_images, test_labels)

#Para mim, isso retornou uma precisão de cerca de 0,8838, o que significa que foi cerca de 88% preciso. Como esperado, provavelmente não funcionaria tão bem com dados invisíveis quanto com os dados nos quais foi treinado! Ao longo deste curso, você verá maneiras de melhorar isso.
classifications = model.predict(test_images)
print(classifications[0])

#Dica: tente executar print(test_labels[0]) - e você obterá um 9. Isso ajuda você a entender por que esta lista tem a aparência que tem?
print(test_labels[0])

#O que esta lista representa?
#São 10 valores aleatórios sem sentido
#São as 10 primeiras classificações que o computador fez
#É a probabilidade de que este item seja cada uma das 10 classes
#Responder:
#A resposta correta é (3)
#A saída do modelo é uma lista de 10 números. Esses números são uma probabilidade de que o valor que está sendo classificado seja o valor correspondente, ou seja, o primeiro valor da lista é a probabilidade de a caligrafia ser '0', o próximo ser '1' etc. Probabilidades BAIXAS.
#Para o 7, a probabilidade era 0,999+, ou seja, a rede neural está nos dizendo que é quase certo que seja um 7.
#Como você sabe que esta lista indica que o item é uma bota?
#Não há informações suficientes para responder a essa pergunta
#O décimo elemento da lista é o maior, e a bota é rotulada como 9
#A bota tem o rótulo 9 e há 0->9 elementos na lista
#Responder
#A resposta correta é (2). Tanto a lista quanto os rótulos são baseados em 0, então a bota com rótulo 9 significa que é a 10ª das 10 classes. A lista com o 10º elemento sendo o valor mais alto significa que a Rede Neural previu que o item que está classificando é provavelmente uma bota de tornozelo
