import cv2
from ultralytics import YOLO
import supervision as sv
from ..format_video.format_time import video_detection_time
from scipy.spatial import distance

def find_centroid(xyxy):
    x1, y1, x2, y2 = xyxy
    cx = (x1 + x2) / 2.0
    cy = (y1 + y2) / 2.0
    return cx, cy

def detect_and_track(model_name, video_path, detection_area = None):
    
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
    people_velocity = {}
    detections = None

    for result in model.track(source=video_path, stream=True, agnostic_nms=True, classes=[0]):
        frame = result.orig_img

        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

            # contar todas as deteccoes do frame
            for identifier in result.boxes.id:
                id_int = int(identifier)
                if id_int in frames_detect_counter.keys(): 
                    # encontra posicao atual da pessoa
                    actual_position = find_centroid(detections[detections.tracker_id == id_int].xyxy[0])
                    previous_position = people_velocity[id_int]['previous_position_in_frame']

                    # calcular a velocidade da pessoa
                    people_velocity[id_int]['travelled_distance'] = people_velocity[id_int]['travelled_distance'] + distance.euclidean(previous_position, actual_position)
                    people_velocity[id_int]['previous_position_in_frame'] = actual_position
                    
                    frames_detect_counter[id_int] = frames_detect_counter[id_int] + 1
                else:
                    frames_detect_counter[id_int] = 1

                    people_velocity[id_int] = {
                        'travelled_distance': 0,
                        'previous_position_in_frame': find_centroid(detections[detections.tracker_id == id_int].xyxy[0])
                    }
        


        detections = detections[(detections.class_id == 0)]

        # desenhar apenas as deteccoes que estao dentro da area de interesse
        if detection_area is not None:

            # desenha o retangulo da area de interesse
            cv2.rectangle(frame, (detection_area['x']['min'], detection_area['y']['min']), (detection_area['x']['max'], detection_area['y']['max']), (0, 255, 0), 2)

            xmin = detections.xyxy[:, 0]
            ymin = detections.xyxy[:, 1]
            xmax = detections.xyxy[:, 2]
            ymax = detections.xyxy[:, 3]

            condition = ((xmax > detection_area['x']['min']) & (ymax > detection_area['y']['min'])) & ((xmin < detection_area['x']['max']) & (ymin < detection_area['y']['max']))

            detections = detections[condition]
    
        labels = [
            f"{tracker_id}"
            for _, _ , _, tracker_id
            in detections
        ]

        # Desenhar no frame o quadro com as detecções
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            labels=labels
        )

        # Escreve o quadro processado no arquivo de vídeo de saída
        output_video.write(frame)
        cv2.imshow(model_name, frame)

        if (cv2.waitKey(30) == 27):
            break
        
    # calcular a velocidade de cada pessoa
    for id in people_velocity.keys():
        people_velocity[id]['velocity'] = people_velocity[id]['travelled_distance'] / video_detection_time(frames_detect_counter[id], fps)

    # Salva as informações das detecções
    info_detections = {
        'id': frames_detect_counter.keys(),
        'frames_counter': frames_detect_counter,
        'detection_time': video_detection_time(frames_detect_counter, fps),
    }

    # Libera os objetos do vídeo e fecha a janela
    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()

    return info_detections