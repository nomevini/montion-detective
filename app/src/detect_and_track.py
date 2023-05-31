import cv2
from ultralytics import YOLO
import supervision as sv
from format_time import video_detection_time, seconds_to_time
from scipy.spatial import distance

def find_centroid(xyxy):
    x1, y1, x2, y2 = xyxy
    cx = (x1 + x2) / 2.0
    cy = (y1 + y2) / 2.0
    return cx, cy

def detect_and_track(model_name, video_path, detection_area = None, frame_a_frame = False):
    
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

    # Numero atual do frame
    frame_number = 0

    # Informacoes das deteccoes de todos os frames (caso analise frame a frame esteja ativado)
    info_detections = {}
    final_people_velocity = {}

    for result in model.track(source=video_path, stream=True, agnostic_nms=True, classes=[0]):
        frame_number += 1
        frame = result.orig_img
        
        detections = sv.Detections.from_yolov8(result)

        detections = detections[(detections.class_id == 0)]

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

                    # calcular a velocidade da pessoa (isso aqui não pode usar a funcao de video)
                    '''
                    people_velocity[id_int]['velocity'] = people_velocity[id_int]['travelled_distance'] / video_detection_time(frames_detect_counter[id_int], fps)
                    '''
                    
                    # calcular a velocidade da pessoa
                    seconds = frames_detect_counter[id_int] / fps
                    people_velocity[id_int]['velocity'] = people_velocity[id_int]['travelled_distance'] / seconds

                    frames_detect_counter[id_int] = frames_detect_counter[id_int] + 1
                else:
                    frames_detect_counter[id_int] = 1

                    people_velocity[id_int] = {
                        'travelled_distance': 0,
                        'previous_position_in_frame': find_centroid(detections[detections.tracker_id == id_int].xyxy[0]),
                        'velocity': 0
                    }
        
        

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
            for tracker_id
            in detections.tracker_id
        ]

        # Desenhar no frame o quadro com as detecções
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            labels=labels
        )

        # reorganizar as informacoes de velocity
        for id, velocity_person in people_velocity.items():
            final_people_velocity[id] = velocity_person["velocity"]


        # salvar as informacoes das deteccoes frame a frame

        if frame_a_frame:
            info_detections[frame_number] = {
                'id': detections.tracker_id,
                'frames_counter': frames_detect_counter,
                'detection_time': video_detection_time(frames_detect_counter, fps),
                'velocity': final_people_velocity
            }


        # Escreve o quadro processado no arquivo de vídeo de saída
        output_video.write(frame)
        cv2.imshow(model_name, frame)

        if (cv2.waitKey(30) == 27):
            break

    info_detections['full_video'] = {
        'id': frames_detect_counter.keys(),
        'frames_counter': frames_detect_counter,
        'detection_time': video_detection_time(frames_detect_counter, fps),
        'velocity': final_people_velocity
    }

    # Libera os objetos do vídeo e fecha a janela
    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()

    return info_detections


if __name__ == '__main__':
    infos = detect_and_track('yolov8n', 'pedestrian_cut_640x320_7_fps.mp4', frame_a_frame=True)
    
    # imprime as informacoes das deteccoes
    for frame, deteccoes in infos.items():
        print(f'frame: {frame}')
        print(f'deteccoes: {deteccoes}')
        print('\n')
        print('\n')
        print('\n')
