import cv2
import numpy as np
from collections import defaultdict
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import time

def resize_frame(frame, new_width):
    """
    Redimensiona o quadro para a largura desejada, mantendo a proporção original.
    
    Parâmetros:
        frame: O quadro de entrada.
        new_width: A nova largura desejada.
        
    Retorna:
        O quadro redimensionado.
    """
    # Obter dimensões originais
    height, width, _ = frame.shape
    
    # Calcular a nova altura mantendo a proporção
    new_height = int((new_width / width) * height)
    
    # Redimensionar o quadro
    return cv2.resize(frame, (new_width, new_height))

def draw_boxes(frame, results, track_history):
    """
    Desenha os retângulos delimitadores (boxes) e outras informações relevantes no frame.
    
    Parâmetros:
        frame: O quadro de entrada.
        results: Resultados da detecção (saída do modelo YOLO).
        track_history: Dicionário para armazenar o histórico de rastreamento.
        
    Retorna:
        O frame com os retângulos delimitadores desenhados.
    """
    boxes = results[0].boxes.xyxy.cpu()
    
    if results[0].boxes.id is not None:
        track_ids = results[0].boxes.id.int().cpu().tolist()

        for box, track_id in zip(boxes, track_ids):
            # Desenhar retângulo vermelho ao redor da detecção
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 0, 255), 2)
            # Escrever o ID no retângulo
            text = f"{track_id}"
            (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            cv2.rectangle(frame, (int(box[0]), int(box[1]) - text_height - 10), (int(box[0]) + text_width + 10, int(box[1])), (0, 0, 255), -1)
            cv2.putText(frame, text, (int(box[0]) + 5, int(box[1]) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            # Armazenar histórico de rastreamento
            track = track_history[track_id]
            track.append((int((box[0] + box[2]) / 2), int((box[1] + box[3]) / 2)))
            if len(track) > 30:
                track.pop(0)

    return frame


def process_video(video_path, model, new_width, target_fps, main_window=None, thread_running=None):
    """
    Processa um fluxo de vídeo de uma câmera de rede com a redução de resolução e a taxa de quadros desejada.
    
    Parâmetros:
        video_path: O URL do fluxo de vídeo da câmera de rede.
        model: Modelo de detecção YOLO.
        new_width: A nova largura desejada para os quadros redimensionados.
        target_fps: A taxa de quadros desejada (em frames por segundo).
        main_window: Tela no pyqt5 para transmitir o frame
    """

    track_history = defaultdict(lambda: [])
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video stream"
    
    # Configurações de tempo para atingir a taxa de quadros desejada
    frame_interval = 1 / target_fps  # Intervalo de tempo entre os quadros desejados
    prev_time = time.time() - frame_interval  # Inicializa o tempo anterior
    while cap.isOpened() and thread_running[0]:
        success, frame = cap.read()
        people_counter = 0
        
        if success:
            current_time = time.time()
            if current_time - prev_time >= frame_interval:
                prev_time = current_time
                
                # Redimensionar o quadro
                frame_resized = resize_frame(frame, new_width)
                
                # Processar o quadro redimensionado
                results = model.track(frame_resized, persist=True, verbose=False, classes=[0]) # definir conf
                frame_resized_drawed = draw_boxes(frame_resized, results, track_history)

                if results[0].boxes.id is not None:
                    people_counter = len(results[0].boxes.id)

                if main_window:
                    main_window.update_image(frame_resized_drawed, people_counter)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

# Exemplo de uso:
#model = YOLO("yolov8n.pt")
#process_video(0, model, new_width=640, target_fps=5)
