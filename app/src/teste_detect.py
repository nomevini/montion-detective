from app.src.detect_and_track import detect_and_track

infos = detect_and_track('yolov8n', video_path='app/src/detect/pedestrian_cut_640x320_10_fps.mp4', detection_area=None)