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