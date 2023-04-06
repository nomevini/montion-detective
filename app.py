import argparse
import norfair

from norfair import Tracker, Video

from tracking.norfair_detections import yolo_detections_to_norfair_detections
from detect_people.yolo import YOLO

DISTANCE_THRESHOLD_BBOX: float = 0.7
DISTANCE_THRESHOLD_CENTROID: int = 30
MAX_DISTANCE: int = 10000

parser = argparse.ArgumentParser(description="Track objects in a video.")
parser.add_argument("files", type=str, nargs="+", help="Video files to process")
parser.add_argument(
    "--model-name", type=str, default="yolov5n", help="YOLOv5 model name"
)
parser.add_argument(
    "--img-size", type=int, default="640", help="YOLOv5 inference size (pixels)"
)
parser.add_argument(
    "--conf-threshold",
    type=float,
    default="0.30",
    help="YOLOv5 object confidence threshold",
)
parser.add_argument(
    "--iou-threshold", type=float, default="0.45", help="YOLOv5 IOU threshold for NMS"
)
parser.add_argument(
    "--classes",
    nargs="+",
    type=int,
    help="Filter by class: --classes 0, or --classes 0 2 3",
)
parser.add_argument(
    "--device", type=str, default=None, help="Inference device: 'cpu' or 'cuda'"
)
parser.add_argument(
    "--track-points",
    type=str,
    default="centroid",
    help="Track points: 'centroid' or 'bbox'",
)
args = parser.parse_args()

model = YOLO(args.model_name, device=args.device)

for input_path in args.files:
    video = Video(input_path=input_path)

    distance_function = "iou" if args.track_points == "bbox" else "euclidean"
    distance_threshold = (
        DISTANCE_THRESHOLD_BBOX
        if args.track_points == "bbox"
        else DISTANCE_THRESHOLD_CENTROID
    )

    tracker = Tracker(
        distance_function=distance_function,
        distance_threshold=distance_threshold,
    )

    for frame in video:
        yolo_detections = model(
            frame,
            conf_threshold=args.conf_threshold,
            iou_threshold=args.iou_threshold,
            image_size=args.img_size,
            classes=args.classes,
        )
        detections = yolo_detections_to_norfair_detections(
            yolo_detections, track_points=args.track_points
        )
        tracked_objects = tracker.update(detections=detections)
        if args.track_points == "centroid":
            #norfair.draw_points(frame, detections)
            norfair.draw_tracked_objects(frame, tracked_objects)
        elif args.track_points == "bbox":
            #norfair.draw_boxes(frame, detections)
            norfair.draw_tracked_boxes(frame, tracked_objects)
        video.write(frame)