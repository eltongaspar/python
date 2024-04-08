#Temp

#Exercicio  65 
#Reconhecimento de emocoes 

#Impostando as bibliotecas
import cv2
# A importação do OpenCV está correta. Você pode usar o OpenCV para uma variedade de tarefas de processamento de imagem e visão computacional.
import numpy as np
#NumPy é uma biblioteca fundamental em Python para computação numérica e é frequentemente usada em conjunto com o OpenCV para manipulação de matrizes e arrays.
import pandas as pd
# Pandas é uma biblioteca de análise de dados em Python e pode ser útil para manipular e analisar dados estruturados.
#from google.colab.patches import cv2_imshow
#Esta função é específica para o ambiente de notebook do Google Colab e não está disponível em ambientes locais. Se você estiver usando o Google Colab, pode usar essa função para exibir imagens diretamente no notebook.
import zipfile
#Esta biblioteca é usada para trabalhar com arquivos zip em Python
import matplotlib.pyplot as plt
# amplamente utilizada para plotar gráficos em Python. 
#%tensorflow_version 2.x
#Parece que você está usando o ambiente do Google Colab e está tentando definir a versão do TensorFlow para 2.x. No Google Colab, você pode definir a versão do TensorFlow usando a mágica 

#Impostando as bibliotecas
import tensorflow as tf
import keras
#Importar a biblioteca TensorFlow
from tensorflow.keras.models import load_model
# Importar a função para carregar modelos previamente treinados
from tensorflow.keras.preprocessing.image import img_to_array
# Importar a função para converter uma imagem em uma matriz
#tensorflow.__version__

print("Versão do TensorFlow:", tf.__version__)
print("Versão do Keras:", keras.__version__)


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


# Conectando o Colab ao Google Drive
#from google.colab import drive
#drive.mount('/content/gdrive')

# Realize o dowload da pasta Material_complementar_reconhecimento_emocoes.zip do Google Sala de Aula e transfira-a para o seu Google Drive
# Localize o caminho da pasta no menu Arquivos, no menu lateral esquerdo
#path = "/content/gdrive/MyDrive/Material_complementar_reconhecimento_emocoes.zip"
#zip_object = zipfile.ZipFile(file = path, mode = "r")
#zip_object.extractall('./')
#zip_object.close

# Gera um numero aleatorio de 1 a 4 para os diretorios 
# Por funcao retorma o numero o numero aleatorio
num_ger = num_aleat(1,2)

if num_ger == 1 or num_ger == 2:
    caminho_da_pasta = 'D:/Dados/Material_complementar_reconhecimento_emocoes/testes/'

# Apos diretorio aleatorio, escolhe arquivo aleatorio para analise
# Assim é possivel juntar mais de um diretório
arquivo_aleatorio = escolher_arquivo_aleatorio(caminho_da_pasta)
print("Arquivo escolhido aleatoriamente:", arquivo_aleatorio)

# Selecione uma imagem da pasta "testes" para o reconhecimento da emoção
imagem = cv2.imread(arquivo_aleatorio) 
#cv2_imshow(imagem)
# Exibe a imagem
plt.imshow(imagem)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()
#imagem.show()

#Testando o Detector
#Carregamento dos modelos
# Utilize um haarcasdade pré treinado para o reconhecimento facial
# Utilize um modelo pré treinado para o reconhecimento das emoções

#Carreganos os diretorios de imagens e modelos 
# Caminhos dos arquivos
dir_cascade_faces =  'D:/Dados/Material_complementar_reconhecimento_emocoes/haarcascade_frontalface_default.xml'
dir_modelo_emotion = 'D:/Dados/Material_complementar_reconhecimento_emocoes/modelo_01_expressoes.h5'

# Outras partes do seu código aqui (por exemplo, carregar o classificador de faces, etc.)
cascade_faces = dir_cascade_faces
caminho_modelo = dir_modelo_emotion
face_detection = cv2.CascadeClassifier(cascade_faces)


classificador_emocoes = load_model(caminho_modelo, compile=False)
expressoes = ["Raiva", "Nojo", "Medo", "Feliz", "Triste", "Surpreso", "Neutro"]  # Expressões identificadas pelo modelo

#Detecção de faces
# Detecta faces na imagem selecionada
original = imagem.copy()
faces = face_detection.detectMultiScale(original, scaleFactor = 1.1,
                                        minNeighbors = 3, minSize = (20,20))

# Apresentação do array representando a localização (em pixels) das faces encontradas
faces

# Quantidade de faces encontradas pelo modelo
len(faces)

#Extração do ROI (região de interesse)
# Convertendo a imagem em escala de cinza
cinza = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
plt.imshow(imagem)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

# Especificação da região de interesse, conforme a face detecada.
# Retome a apresentação do array para especificar a regição de interesse. Ex: [381, 149, 140, 140]
# Na posição do pixel 149, some 140 e, também, à posição do pixel 381, some 140.
roi = cinza[149:149 + 140, 381:381 + 140]
#cv2_imshow(roi)
plt.imshow(imagem)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

# Redimensionando a ROI
roi = cv2.resize(roi, (48, 48))
plt.imshow(imagem)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

# Normalizando a ROI
roi = roi / 255

# Transformando a imagem da ROI em array
roi = img_to_array(roi)

# Expandindo as dimensões da ROI
roi = np.expand_dims(roi, axis = 0)

# Forma da ROI: (quantidade de imagens, pixel x, pixel y, quantidade de canais)
roi.shape

# Levantando as predições do classificador de emoções
preds = classificador_emocoes.predict(roi)[0]
preds

# Quandidade de predições encontradas (referente a cada uma das 7 categorias de emoções)
len(preds)

# Retorno da predição com maior probabilidade
emotion_probability = np.max(preds)
emotion_probability

# Categoria da máxima predição
preds.argmax()

# Demonstrando a categoria na classe correspondente
label = expressoes[preds.argmax()]
label


# Escrevendo a emoção na imagem original
# Desenhando um retângulo na face encontrada
cv2.putText(original, label, (381, 149 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
            (0, 0, 255), 2, cv2.LINE_AA)
cv2.rectangle(original, (381, 149), (381 + 140, 149 + 140), (0, 0, 255), 2)
plt.imshow(imagem)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

probabilidades = np.ones((250,300,3), dtype= 'uint8') * 255 #inteiro


# Demonstrando as probabilidades das categorias em barras
plt.imshow(original)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

if len(faces) == 2:
  for (i, (emotion, prob)) in enumerate(zip(expressoes, preds)):
    #print(i, emotion, prob)
    text = "{}: {:.2f}%".format(emotion, prob * 100)
    w = int(prob * 300)
    cv2.rectangle(probabilidades, (7, (i * 35) + 5), (w, (i * 35) + 35), (200, 250, 20), -1)
    cv2.putText(probabilidades, text, (10, (i * 35) + 23), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 1, cv2.LINE_AA)
plt.imshow(probabilidades)
plt.axis('off')  # Desativar eixos para uma visualização mais limpa
plt.show()

