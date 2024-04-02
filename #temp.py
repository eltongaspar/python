#Temp 


# Exercicio 64 
#Classificador de Imagens caes e gatos 

#Importando as bibliotecas 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import numpy as np
import cv2
#from google.colab.patches import cv2_imshow
tf.__version__
import os
import random
from PIL import Image

# Conexão do Google Colava à pasta do Google Drive, local onde deverá ter salvo a pasta caes-e-gatos.zip
#from google.colab import drive
#drive.mount('/content/drive')
# Descompactar a pasta caes-e-gatos na pasta de Arquivos do Google Colab
#path = '/content/drive/MyDrive/caes-e-gatos.zip'
#zip_object = zipfile.ZipFile(file=path, mode='r')
#zip_object.extractall('./')
#zip_object.close()

#Carregamento das imagens
# Localizar o caminho da primeira imagem de gato na pasta treinamento
cat_arq_ini = 'D:/Dados/caes e gatos full/Treinamento/gato/0.jpg'
tf.keras.preprocessing.image.load_img(cat_arq_ini)

# Localizar o caminho da primeira imagem de cão na pasta treinamento
dog_arq_ini = 'D:/Dados/caes e gatos full/Treinamento/cao/0.jpg'
tf.keras.preprocessing.image.load_img(dog_arq_ini)

#Base de treinamento e teste
# Localizar as 4000 imagens, nas duas classes para a base de treinamento
dir_train = 'D:/Dados/caes e gatos full/Treinamento/'
gerador_treinamento = ImageDataGenerator(rescale=1./255,
                                        rotation_range=7,
                                        horizontal_flip=True,
                                        zoom_range=0.2)
dataset_treinamento = gerador_treinamento.flow_from_directory(dir_train,
                                                        target_size = (64, 64),
                                                        batch_size = 32,
                                                        class_mode = 'categorical',
                                                        shuffle = True)



# Estabelecendo índices para as classes no treinamento 0: cão e 1: gato
dataset_treinamento.class_indices                                                        

# Localizar o campinho para a paste de teste, contendo 1000 imagens com as duas classes
dir_test = 'D:/Dados/caes e gatos full/Teste'
gerador_teste = ImageDataGenerator(rescale=1./255)
dataset_teste = gerador_teste.flow_from_directory(dir_test,
                                                     target_size = (64, 64),
                                                     batch_size = 1,
                                                     class_mode = 'categorical',
                                                     shuffle = False)


#Construção e treinamento da rede neural
# Criando cada camada da rede neural, conforme o modelo sequencial da rede neural convolucional
network = Sequential()
network.add(Conv2D(32, (3,3), input_shape = (64,64,3), activation='relu'))
network.add(MaxPooling2D(pool_size=(2,2)))

network.add(Conv2D(32, (3,3), activation='relu'))
network.add(MaxPooling2D(pool_size=(2,2)))

network.add(Flatten())

network.add(Dense(units = 3137, activation='relu'))
network.add(Dense(units = 3137, activation='relu'))
network.add(Dense(units = 2, activation='softmax'))

# Visualizando o modelo com as classes criadas
network.summary()

# Estabelecendo as taxas de perda e acurácia para o modelo
network.compile(optimizer='Adam', loss='categorical_crossentropy', metrics = ['accuracy'])

# Treinando o modelo com 10 épocas de treinamento
# OBSERVAÇÃO: esta execução pode demorar conforme o desempenho de sua máquina
historico = network.fit(dataset_treinamento, epochs=1)

# Avaliação da rede neural
# Estabelecendo índices para as classes no teste 0: cão e 1: gato
dataset_teste.class_indices

# Trazendo ao modelo as predições do treinamento
previsoes = network.predict(dataset_teste)

# Verificando a máxima previsão para as classes
previsoes = np.argmax(previsoes, axis = 1)

# Verificando os dados do modelo treinado
dataset_teste.classes

# Demonstrando a acurácia do modelo treinado
from sklearn.metrics import accuracy_score
accuracy_score(dataset_teste.classes, previsoes)

#OBSERVAÇÃO: o valor demonstrado acima é a precisão do treinamento do modelo. Valores quanto mais próximos de 1, mais precisa será a classificação. Para aumentar a precisão, pode-se retreinar o modelo ou ainda inserir mais imagens para o treinamento

# Atribuindo as classes ao modelo treinado
dataset_teste.class_indices

# Estabelecendo a matriz de confusão para confronto do dados entre as classes
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dataset_teste.classes, previsoes)

# Demonstrando a matriz de confusão
sns.heatmap(cm, annot=True);

# Classificando os dados obtidos
from sklearn.metrics import classification_report
print(classification_report(dataset_teste.classes, previsoes))

# Salvar e carregar a rede neural
# Gerando um arquivo .json com os dados do modelo
model_json = network.to_json()
with open('network.json','w') as json_file:
  json_file.write(model_json)

  # Criando o arquivo de pesos (pesos.hdf5) do treinamento
  dir_salv = 'D:/Dados/caes e gatos full/pesos.hdf5'
from keras.models import save_model
network_saved = save_model(network, dir_salv)

# Visualizando os dados salvos no arquivo .json
with open('network.json', 'r') as json_file:
  json_saved_model = json_file.read()
json_saved_model

# Atribuindo o treinamento ao modelo
network_loaded = tf.keras.models.model_from_json(json_saved_model)
network_loaded.load_weights('pesos.hdf5')
network_loaded.compile(loss = 'categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

# Visualizando o modelo de rede neural
network_loaded.summary()


def escolher_arquivo_aleatorio(caminho_da_pasta):
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(caminho_da_pasta)
    
    # Filtra apenas os arquivos (remove pastas)
    arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho_da_pasta, arquivo))]
    
    # Escolhe um arquivo aleatoriamente
    arquivo_aleatorio = random.choice(arquivos)
    
    # Retorna o caminho completo do arquivo escolhido
    return os.path.join(caminho_da_pasta, arquivo_aleatorio)

# Exemplo de uso
import os
import random
from PIL import Image

def escolher_arquivo_aleatorio(caminho_da_pasta):
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(caminho_da_pasta)
    
    # Filtra apenas os arquivos (remove pastas)
    arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho_da_pasta, arquivo))]
    
    # Escolhe um arquivo aleatoriamente
    arquivo_aleatorio = random.choice(arquivos)
    
    # Retorna o caminho completo do arquivo escolhido
    return os.path.join(caminho_da_pasta, arquivo_aleatorio)


# Funcao Gerar numero
def num_aleat(num_min,num_max):
    import random
    num_ger = random.randrange(num_min,num_max)
    return num_ger


# Exemplo de uso
num_ger = num_aleat(1,4)

if num_ger == 1:
    caminho_da_pasta = 'D:/Dados/caes e gatos full/Teste/Cao'
elif num_ger == 2:
    caminho_da_pasta = 'D:/Dados/caes e gatos full/Teste/Gato'
elif num_ger == 3:
    caminho_da_pasta = 'D:/Dados/caes e gatos full/Treinamento/Cao'
elif num_ger == 4:
    caminho_da_pasta = 'D:/Dados/caes e gatos full/Treinamento/Gato'

arquivo_aleatorio = escolher_arquivo_aleatorio(caminho_da_pasta)
print("Arquivo escolhido aleatoriamente:", arquivo_aleatorio)
# Abre o arquivo de imagem
dir_arq_analise  = arquivo_aleatorio
imagem = Image.open(arquivo_aleatorio)
    
# Exibe a imagem
imagem.show()

# Classificação de uma única imagem
# Na pasta teste, localize qualquer imagem para a classificação, conforme o modelo treinado

#imagem = cv2.imread(cat_arq_ini)
#imagem = cv2.imread('/content/caes-e-gatos/teste/cao/dog.3501.jpg')
#cv2_imshow(imagem)

# Redimensionando a imagem em 64x64 pixels
imagem = imagem.resize((64, 64))
# Exibe a imagem
imagem.show()

# Convertendo em escala de cinza
#imagem = imagem / 255
imagem.convert('L')

# Parâmetros da imagem redimensionada
#imagem = imagem.reshape(-1, 64, 64, 3)
#imagem.shape
largura, altura = imagem.size
canais_de_cores = len(imagem.getbands())

resultado = network_loaded(imagem)
resultado

# Demonstrando a classe que obteve o maior resultado
resultado = np.argmax(resultado)
resultado

# Verificando as classes do modelo
dataset_teste.class_indices

# Categorizando o resultado
if resultado == 0:
  print('Cão')
else:
  print('Gato')