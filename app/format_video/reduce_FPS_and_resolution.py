import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip

def reduzir_resolucao_e_fps(video, fps_novo):
    clip = VideoFileClip(video)
    fps_antigo = clip.fps
    largura_antiga, altura_antiga = clip.w, clip.h

    proporcao = altura_antiga / largura_antiga
    largura_nova = 640
    altura_nova = int(largura_nova * proporcao)

    cap = cv2.VideoCapture(video)
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    fps = fps_novo
    resolucao = (largura_nova, altura_nova)
    proporcao_str = f'{largura_nova}x{altura_nova}'
    nome_saida = f'{video.split(".")[0]}_{proporcao_str}_reduzido.mp4'
    out = cv2.VideoWriter(nome_saida, codec, fps, resolucao)

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

    return nome_saida


novo_video = reduzir_resolucao_e_fps('pedestrian_cut.mp4', 5)