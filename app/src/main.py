from detect.detect_and_track import detect_and_track
from format_video.format_time import print_formatted_time
from format_video.reduce_FPS_and_resolution import reduzir_resolucao_e_fps
from windows.select_image_area import WindowSelectArea, get_coordinates

path_model = "detect/yolov8n.pt"
video_path = "/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/app/src/format_video/videos_resized/pedestrian_cut_640x360_7_fps.mp4"

# seleciona a area de deteccao
# capturar coordenadas da area de deteccao
# coordinates = get_coordinates(video_path)

info_detections = detect_and_track(path_model, video_path)

print(info_detections['id'])
print_formatted_time(info_detections['detection_time'])
print(info_detections['frames_counter'])
