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
import tensorflow
##Importar a biblioteca TensorFlow
from tensorflow.keras.models import load_model
# Importar a função para carregar modelos previamente treinados
from tensorflow.keras.preprocessing.image import img_to_array
# Importar a função para converter uma imagem em uma matriz
tensorflow.__version__


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


#Carreganos os diretprios de imagens e modelos 
dir_imagens = 'D:/Dados/Material_complementar_reconhecimento_emocoes/testes/'
dir_modelo_emotion = 'D:/Dados/Material_complementar_reconhecimento_emocoes/modelo_01_expressoes.h5'

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
plt.show()
plt.imshow(imagem)
#imagem.show()