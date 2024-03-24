# 4.4 - Reconhecimento Facial 

# Captura 

import cv2
import os #listar diretorio
import time

def capturar_imagens(num_imagens,dir):
    # Inicializar a câmera
    cap = cv2.VideoCapture(0)
    
    # Verificar se a câmera está sendo aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    # Loop para capturar o número especificado de imagens
    for i in range(num_imagens):
        # Capturar frame da câmera
        ret, frame = cap.read()

        # Verificar se o frame foi capturado corretamente
        if not ret:
            print(f"Erro ao capturar a imagem {i+1}.")
            continue

        # Mostrar o frame capturado
        cv2.imshow('Capturando Imagens...', frame)

         #Esperar pela tecla 'q' para sair ou 'c' para capturar
        key = cv2.waitKey(0)
        if key & 0xFF == ord('q'):  # Pressione 'q' para sair
            break
        elif key & 0xFF == ord('c'):  # Pressione 'c' para capturar a imagem
            
            # Verificar se o diretório existe, se não, criar
            if not os.path.exists(dir):
                os.makedirs(dir)

            # Salvar a imagem capturada no diretório especificado
            imagem_path = os.path.join(dir, f'imagem_{i}.jpg')
            if cv2.imwrite(imagem_path, frame):
                print(f'Imagem {i+1} capturada e salva em {imagem_path}.')
            else:
                print(f'Erro ao salvar a imagem {i+1}.')

# Liberar os recursos
    cap.release()
    cv2.destroyAllWindows()

#Modo diretorio 
#defindo diretorio das capturas de imagens 
dir = 'D:/Dados/Material_complementar_reconhecimento_facial/capturas'

# Carrega o classificador pré-treinado para detecção de face e de olhos
arq_modelo_face = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_frontalface_default.xml'
arq_modelo_olhos = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_eye.xml'
faces_cascade = cv2.CascadeClassifier(arq_modelo_face)
olhos_cascate = cv2.CascadeClassifier(arq_modelo_olhos)

# Chamar a função para capturar 5 imagens
capturar_imagens(5,dir)



# Listando diretorio 
files = os.listdir(dir)
#Contagem de arquivos 
num_files = len(files)

# Variável para controlar se pelo menos um face foi detectado
faces_detectados = False
olhos_detectados = False

# Loop sobre cada arquivo no diretório
for num_files in files:
    # Verifica se o arquivo é uma imagem
    if num_files.endswith('.jpg') or num_files.endswith('.png'):
        # Carrega a imagem
        imagem = cv2.imread(os.path.join(dir, num_files))
        # Converte a imagem para escala de cinza
        imagem_cinza_face = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_cinza_olhos = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        # Detecta faces e olhos  na imagem
        faces = faces_cascade.detectMultiScale(imagem_cinza_face, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        olhos = olhos_cascate.detectMultiScale(imagem_cinza_olhos, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Se pelo menos um face for detectado
        if len(faces) > 0:
            # Define a variável para indicar que faces foram detectados
            faces_detectados = True
                # Desenha retângulos ao redor dos faces detectados
            for (x, y, w, h) in faces:
                cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # Exibe a imagem com os faces detectados
                cv2.imshow('Faces Detectados', imagem)
                cv2.waitKey(0)

        if len(olhos) > 0:
            # Define a variável para indicar que olhos foram detectados
            olhos_detectados = True
                # Desenha retângulos ao redor dos olhos detectados
            for (x, y, w, h) in olhos:
                cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # Exibe a imagem com os faces detectados
                cv2.imshow('Faces Detectados', imagem)
                cv2.waitKey(0)

# Se nenhum face foi detectado
if not faces_detectados:
    print("Nenhum Face detectado.")

if not olhos_detectados:
    print("Nenhum Olhos detectado.")


cv2.destroyAllWindows()


#Treinamento 

import cv2
import numpy as np
import os

eigenface = cv2.face.EigenFaceRecognizer_create() # traz a função de reconhecimento Eigenface
fisherface = cv2.face.FisherFaceRecognizer_create() # traz a função de reconhecimento Fisherface
lbph = cv2.face.LBPHFaceRecognizer_create() # traz a função de reconhecimento LBPH

# Listando diretorio 
files = os.listdir(dir)
#Contagem de arquivos 
num_files = len(files)


def carregar_imagens(files):
    faces = []
    ids = []
    
    for file in os.listdir(files):
            imagem_face = cv2.imread(file, cv2.IMREAD_GRAYSCALE) # transforma as imagens em escala de cinza
            ids = int(os.path.split(file)[-1].split('.')[1]) # verifica qual o id do identificador criado na captura
            
            faces.append(imagem_face)
            ids.append(ids)
        
    return faces, np.array(ids)

def treinar_eigenfaces(dir):

    dir_cascates = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades'
    # Carregar as imagens e os rótulos
    faces, ids = carregar_imagens(dir)

    # Inicializar o reconhecedor de faces Eigenfaces
    reconhecedor = cv2.face.EigenFaceRecognizer_create()

    # Treinar o reconhecedor de faces
    reconhecedor.train(faces, ids)

    # Salvar o modelo treinado
    reconhecedor.save(dir_cascates + "modelo_eigenfaces.yml")
    print("Modelo treinado e salvo com sucesso.")

# Diretório onde as imagens estão armazenadas (um diretório por pessoa)
diretorio_dados = "dados_de_treinamento"

# Chamar a função para treinar o modelo de Eigenfaces
treinar_eigenfaces(dir)


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


#Reconhecedor_Eigenface

# Importando as bibliotecas
import cv2

arq_modelo_face = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_frontalface_default.xml'

dir_cascates_Eigen = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/classificadorEigen.yml'

detectorFace = cv2.CascadeClassifier(arq_modelo_face) # uso do haarcascade pora detectar face
reconhecedor = cv2.face.EigenFaceRecognizer_create() # traz a função do reconhecedor Eigenface
reconhecedor.read(dir_cascates_Eigen ) # traz o classificador treinado
largura, altura = 200, 200 # dimensão da imagem
font = cv2.FONT_HERSHEY_COMPLEX_SMALL #tipo de letra
camera = cv2.VideoCapture(0) # inicia a webcam para realizar o reconhecimento baseado no classificador

while True:
    conectado, imagem = camera.read() # realiza a leitura pela webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # transfoma a imagem em escala de cinza
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30)) # detecta a face encontrada

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura)) # redimensiona o tamanha da imagem capturada
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2) # desenha o retângulo da detecção
        id, confianca = reconhecedor.predict(imagemFace) # realiza a predição do reconhecimento
        nome = ""
        if id == 1:
            nome = 'sem macara' # reconhecimento sem uso de máscara, conforme reconhecedor
        elif id == 2:
            nome = 'com mascara' # reconhecimento com uso de máscara, conforme reconhecedor
#        elif id == 3:
#        nome = 'com oculos' # crie outras variações se desejar
        cv2.putText(imagem, nome, (x, y + (a + 40)), font, 2, (0, 0, 255)) # escreve o texto do reconhecimento
        cv2.putText(imagem, str(confianca), (x, y + (a + 60)), font, 1, (0, 0, 255)) # escreve o texto do intervalo de confiança

    cv2.imshow("Face", imagem) # mostra o título da janela
    if cv2.waitKey(1) == ord('q'): # interrompe apertando a tecla Q
        break

camera.release()
cv2.destroyAllWindows()




#Reconhecedor_Fisherface

# Importando as bibliotecas
import cv2

arq_modelo_face = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_frontalface_default.xml'

dir_cascates_Fisher = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/classificadorFisher.yml'

detectorFace = cv2.CascadeClassifier(arq_modelo_face) # uso do haarcascade pora detectar face
reconhecedor = cv2.face.FisherFaceRecognizer_create() # traz a função do reconhecedor Fisherface
reconhecedor.read(dir_cascates_Fisher ) # traz o classificador treinado
largura, altura = 200, 200 # dimensão da imagem
font = cv2.FONT_HERSHEY_COMPLEX_SMALL # tipo de letra
camera = cv2.VideoCapture(0) # inicia a webcam para realizar o reconhecimento baseado no classificador

while True:
    conectado, imagem = camera.read() # realiza a leitura pela webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # transfoma a imagem em escala de cinza
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30)) # detecta a face encontrada

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura)) # redimensiona o tamanha da imagem capturada
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2) # desenha o retângulo da detecção
        id, confianca = reconhecedor.predict(imagemFace) # realiza a predição do reconhecimento
        nome = ""
        if id == 1:
            nome = 'sem mascara' # reconhecimento sem uso de máscara, conforme reconhecedor
        elif id == 2:
            nome = 'com mascara' # reconhecimento com uso de máscara, conforme reconhecedor
        cv2.putText(imagem, nome, (x, y + (a + 40)), font, 2, (0, 0, 255)) # escreve o texto do reconhecimento
        cv2.putText(imagem, str(confianca), (x, y + (a + 60)), font, 1, (0, 0, 255)) # escreve o texto do intervalo de confiança

    cv2.imshow("Face", imagem) # mostra o título da janela
    if cv2.waitKey(1) == ord('q'): # interrompe apertando a tecla Q
        break

camera.release()
cv2.destroyAllWindows()


#Reconhecedor_LBPH

# Importando as bibliotecas
import cv2

arq_modelo_face = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_frontalface_default.xml'

dir_cascates_LBPH = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/classificadorLBPH.yml'

detectorFace = cv2.CascadeClassifier(arq_modelo_face) # uso do haarcascade pora detectar face
reconhecedor = cv2.face.LBPHFaceRecognizer_create() # traz a função do reconhecedor Eigenface
reconhecedor.read(dir_cascates_LBPH) # traz o classificador treinado
largura, altura = 200, 200 # dimensão da imagem
font = cv2.FONT_HERSHEY_COMPLEX_SMALL # tipo de letra
camera = cv2.VideoCapture(0) # inicia a webcam para realizar o reconhecimento baseado no classificador

while True:
    conectado, imagem = camera.read() # realiza a leitura pela webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # transfoma a imagem em escala de cinza
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30)) # detecta a face encontrada

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura)) # redimensiona o tamanha da imagem capturada
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2) # desenha o retângulo da detecção
        id, confianca = reconhecedor.predict(imagemFace) # realiza a predição do reconhecimento
        nome = ""
        if id == 1:
            nome = 'sem macara' # reconhecimento sem uso de máscara, conforme reconhecedor
        elif id == 2:
            nome = 'com mascara' # reconhecimento com uso de máscara, conforme reconhecedor
        cv2.putText(imagem, nome, (x, y + (a + 40)), font, 2, (0, 0, 255)) # escreve o texto do reconhecimento
        cv2.putText(imagem, str(confianca), (x, y + (a + 60)), font, 1, (0, 0, 255)) # escreve o texto do intervalo de confiança

    cv2.imshow("Face", imagem) # mostra o título da janela
    if cv2.waitKey(1) == ord('q'): # interrompe apertando a tecla Q
        break

camera.release()
cv2.destroyAllWindows()

