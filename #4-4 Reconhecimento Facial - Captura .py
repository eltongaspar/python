 #4-4 Reconhecimento Facial Model
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


