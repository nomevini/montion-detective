from detect.detect_and_track import detect_and_track
from format_video.format_time import print_formatted_time
from format_video.reduce_FPS_and_resolution import reduzir_resolucao_e_fps

path_model = "detect/yolov8n.pt"
video_path = "/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/app/assets/videos/pedestrian_cut.mp4"





info_detections = detect_and_track(path_model, video_path)

print_formatted_time(info_detections)