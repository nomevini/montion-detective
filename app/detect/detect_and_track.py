import cv2
from ultralytics import YOLO
import supervision as sv
from format_video.format_time import video_detection_time

def detect_and_track(model_name, video_path):
    
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    model = YOLO(model_name)

    # Abre o vídeo de entrada e obtem as configurações
    input_video = cv2.VideoCapture(video_path)
    fps = input_video.get(cv2.CAP_PROP_FPS)
    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define o codec e as configurações do vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

    # contar os frames que cada deteccao apareceu
    frames_detect_counter = {}

    for result in model.track(source=video_path, stream=True, agnostic_nms=True, classes=[0]):
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
            
            # contar todas as deteccoes do frame
            for identifier in result.boxes.id:
                id_int = int(identifier)
                if id_int in frames_detect_counter.keys(): 
                    frames_detect_counter[id_int] = frames_detect_counter[id_int] + 1
                else:
                    frames_detect_counter[id_int] = 1

        detections = detections[(detections.class_id == 0)]

        
        labels = [
            f"{tracker_id} {confidence:0.2f}"
            for _, confidence , _, tracker_id
            in detections
        ]

        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            labels=labels
        )

        # Escreve o quadro processado no arquivo de vídeo de saída
        output_video.write(frame)
        cv2.imwrite('nova_imagem.png', frame)
        
        cv2.imshow(model_name, frame)

        if (cv2.waitKey(30) == 27):
            break
            
    # calcular o tempo que cada deteccao permaneceu no vídeo
    info_detections = video_detection_time(frames_detect_counter, fps)

    # Libera os objetos do vídeo e fecha a janela
    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()

    return info_detections