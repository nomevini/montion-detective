import cv2

from ultralytics import YOLO
import supervision as sv
import numpy as np


LINE_START = sv.Point(320, 0)
LINE_END = sv.Point(320, 480)


def main():
    line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    model = YOLO("yolov8n.pt")
    for result in model.track(source="/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/yolov8/pedestrian_cut_640x360_reduzido.mp4", show=False, stream=True, agnostic_nms=True, classes=[0]):
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

        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break


if __name__ == "__main__":
    main()