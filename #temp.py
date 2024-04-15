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
