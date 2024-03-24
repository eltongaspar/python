#4-4

#Treinamento

#Importando as bibliotecas
import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create() # traz a função de reconhecimento Eigenface
fisherface = cv2.face.FisherFaceRecognizer_create() # traz a função de reconhecimento Fisherface
lbph = cv2.face.LBPHFaceRecognizer_create() # traz a função de reconhecimento LBPH

dir = 'D:/Dados/Material_complementar_reconhecimento_facial/capturas'

def getImagemComId():
    caminhos = [os.path.join(dir, f) for f in os.listdir(dir)] # irá percorrer todas as imagens da pasta fotos criada na captura
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY) # transforma as imagens em escala de cinza
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1]) # verifica qual o id do identificador criado na captura
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

ids, faces = getImagemComId()

dir_cascates = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/'

print("Treinando...") # indicação que está havendo o treinamento, conforme o reconhecedor
eigenface.train(faces, ids)
eigenface.write(dir_cascates +  'classificadorEigen.yml') # realiza o treinamento e cria o classificador Eingeface

fisherface.train(faces, ids)
fisherface.write(dir_cascates + 'classificadorFisher.yml') # realiza o treinamento e cria o classificador Fisherface

lbph.train(faces, ids)
lbph.write(dir_cascates + 'classificadorLBPH.yml') # realiza o treinamento e cria o classificador LBPH

print("Treinamento realizado") # indica que o treinamento foi finalizado
#depois de treinado ele vai gerar os arquivos que vão aparecer no menu ao lado e serão utilizados para o algoritmo de reconhecimento