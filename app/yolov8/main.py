import cv2

from ultralytics import YOLO
import supervision as sv
import numpy as np

LINE_START = sv.Point(320, 0)
LINE_END = sv.Point(320, 480)

def main():

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    model = YOLO("yolov8n.pt")

    # Abre o vídeo de entrada e obtem as configurações
    input_video = cv2.VideoCapture('/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/yolov8/pedestrian_cut_640x360.mp4')
    fps = input_video.get(cv2.CAP_PROP_FPS)
    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define o codec e as configurações do vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

    for result in model.track(source="/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/yolov8/pedestrian_cut_640x360.mp4", stream=True, agnostic_nms=True, classes=[0]):
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        
        detections = detections[(detections.class_id == 0)]

        labels = [
            f"{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, tracker_id
            in detections
        ]

        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            labels=labels
        )

        # Escreve o quadro processado no arquivo de vídeo de saída
        output_video.write(frame)

        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break

    # Libera os objetos do vídeo e fecha a janela
    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()