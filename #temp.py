#Temp

#Exercicio  65 
#Reconhecimento de emocoes 

#Impostando as bibliotecas
import cv2
import numpy as np
import pandas as pd
#from google.colab.patches import cv2_imshow
import zipfile
#Carreganos os diretprios de imagens e modelos 
dir_imagens = 'D:/Dados/Material_complementar_reconhecimento_emocoes/testes/'
dir_modelo_emotion = 'D:/Dados/Material_complementar_reconhecimento_emocoes/modelo_01_expressoes.h5'