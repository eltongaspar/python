#Temp

#Exercicio  68
#Rastreamento de objetos unicos 


import cv2

# Carregar o vídeo
video_path = 'D:/Dados/Material_complementar_rastreamento_objetos/videos/race.mp4'
cap = cv2.VideoCapture(video_path)

# Inicializar o rastreador
tracker = cv2.TrackerCSRT_create()

# Ler o primeiro frame do vídeo
ret, frame = cap.read()
if not ret:
    print("Erro ao ler o vídeo")
    exit()

# Selecionar a região de interesse (ROI) para rastrear
bbox = cv2.selectROI("Selecione o objeto a ser rastreado", frame, False)
tracker.init(frame, bbox)

while True:
    # Ler o próximo frame do vídeo
    ret, frame = cap.read()
    if not ret:
        break
    
    # Atualizar o rastreador com o novo frame
    success, bbox = tracker.update(frame)
    
    # Desenhar a região rastreada no frame
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Perda de rastreamento", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    # Exibir o frame com a região rastreada
    cv2.imshow("Rastreamento de objeto", frame)
    
    # Verificar se o usuário pressionou a tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o objeto de captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()

#Exercicio  69
#Rastreamento de objetos multiplos 


import cv2

# Carregar o vídeo
video_path = 'D:/Dados/Material_complementar_rastreamento_objetos/videos/race.mp4'
cap = cv2.VideoCapture(video_path)

# Inicializar o rastreador de objetos (utilizando um classificador de Haar para detecção)
tracker = cv2.MultiTracker_create()

# Ler o primeiro frame do vídeo
ret, frame = cap.read()

# Selecionar as regiões de interesse (ROI) para rastrear
rois = cv2.selectROIs("Selecione as ROIs", frame)
for roi in rois:
    tracker.add(cv2.TrackerCSRT_create(), frame, tuple(roi))

# Loop para rastrear os objetos em cada frame do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Atualizar o rastreamento dos objetos
    success, boxes = tracker.update(frame)
    
    # Desenhar retângulos ao redor dos objetos rastreados
    if success:
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Mostrar o frame com os objetos rastreados
    cv2.imshow('Multi-object Tracking', frame)
    
    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()