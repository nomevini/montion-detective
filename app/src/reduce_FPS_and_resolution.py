import cv2
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

class FormatVideo:

    def reduce_resolution_and_fps(self, video, dimensao_nova=(640, None), fps_novo=8):
        try:
            clip = VideoFileClip(video)
            fps_antigo = clip.fps
            largura_antiga, altura_antiga = clip.w, clip.h

            if fps_novo == None:
                fps_novo = fps_antigo

            if dimensao_nova[0] is not None and dimensao_nova[1] is not None:
                largura_nova, altura_nova = dimensao_nova
            else:
                largura_nova = largura_antiga
                altura_nova = altura_antiga

            cap = cv2.VideoCapture(video)
            codec = cv2.VideoWriter_fourcc(*"mp4v")
            fps = fps_novo
            resolucao = (largura_nova, altura_nova)
            proporcao_str = f'{largura_nova}x{altura_nova}'

            path_out = "app/src/videos_resized"

            # criar diretorio caso nao exista
            if not os.path.exists(path_out):
                os.makedirs(path_out, exist_ok=True)

            video_name = video.split("/")[-1]
            video_name_without_extension = video_name.split(".")[0]
            path_video_out = f"{path_out}/{video_name_without_extension}_{proporcao_str}_{fps_novo}_fps.mp4"
            out = cv2.VideoWriter(path_video_out, codec, fps, resolucao)

            n_frames_pular = int(fps_antigo / fps_novo)
            count = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                if count % n_frames_pular == 0:
                    frame_redimensionado = cv2.resize(frame, resolucao)
                    out.write(frame_redimensionado)
                count += 1

            cap.release()
            out.release()

            return path_video_out
        except OSError:
            print("\nArquivo não encontrado!")