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



