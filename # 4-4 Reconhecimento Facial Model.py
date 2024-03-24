# 4-4 Reconhecimento Facial Model
#Modelo 

#Captura 

# 4.4 - Reconhecimento Facial 

# Importando as bibliotecas
import cv2
import numpy as np

#Modo diretorio 
#defindo diretorio das capturas de imagens 
dir = 'D:/Dados/Material_complementar_reconhecimento_facial/capturas/'

# Carrega o classificador pré-treinado para detecção de face e de olhos
arq_modelo_face = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_frontalface_default.xml'
arq_modelo_olhos = 'D:/Dados/Material_complementar_reconhecimento_facial/cascades/haarcascade_eye.xml'

classificador = cv2.CascadeClassifier(arq_modelo_face) # utilizando o haarcascade para detectar a face
classificadorOlho = cv2.CascadeClassifier(arq_modelo_olhos) # utilizando o haarcascade para detectar olhos
camera = cv2.VideoCapture(0) # 0 siginifica que irá usar a câmera padrão e 1 webcam externa
amostra = 1
numeroAmostras = 25 # captura de 25 imagens da face, varie a posição ao capturar
id = input('Digite seu identificador: ') # comece com o identificador #1 para realizar captura sem máscara e #2 para com máscara
largura, altura = 200, 200 # dimensões das imagens capturadas
print("Capturando as faces...") # indicação de início da captura

while True:
    conectado, imagem = camera.read() # captura das imagens pela webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # transformação das imagens em escala de cinza
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100)) # detecta face nas imagens capturadas

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2) # desenha um retângulo na face detectada
        regiao = imagem[y:y + a, x:x + l] # dimensões do retângulo
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2) # desenha um retângulo nos olhos detectados

        if cv2.waitKey(1) & 0xFF == ord('q'): # aperte a tecla Q para realizar as capturas das imagens
            if np.average(imagemCinza) > 100:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                # criar a pasta fotos: New > Directory > fotos
                cv2.imwrite(dir + str(id) + "." + str(amostra) + ".jpg", imagemFace) # nomeia as imagens capturadas
                print("[foto " + str(amostra) + " capturada com sucesso]")
                amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    if amostra >= numeroAmostras + 1:
        break

print("Faces capturadas com sucesso") # mensagem de finalização da captura das 25 imagens
camera.release()
cv2.destroyAllWindows()


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