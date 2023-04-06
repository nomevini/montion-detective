import os
import cv2

def diminuir_resolucao(video_path, largura_desejada, altura_desejada):
    if not os.path.exists(video_path):
        raise FileNotFoundError("Arquivo de vídeo não encontrado")

    video = cv2.VideoCapture(video_path)

    # obter a taxa de frames do vídeo original
    taxa_frames = video.get(cv2.CAP_PROP_FPS)

    # obter a largura e altura do vídeo original
    largura_original = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_original = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # criar um objeto VideoWriter para gravar o novo vídeo
    novo_video_path = f"diminuido_{largura_desejada}x{altura_desejada}_{video_path}"
    codec = cv2.VideoWriter_fourcc(*'mp4v') # usar codec MP4V para gravar o novo vídeo
    novo_video = cv2.VideoWriter(novo_video_path, codec, taxa_frames, (largura_desejada, altura_desejada))

    # ler cada frame do vídeo original, redimensioná-lo e gravar o novo vídeo
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame_redimensionado = cv2.resize(frame, (largura_desejada, altura_desejada))
        novo_video.write(frame_redimensionado)

    # liberar os recursos utilizados
    video.release()
    novo_video.release()
    cv2.destroyAllWindows()

    return novo_video_path

video_path = "pedestrian_cut.mp4"
largura_desejada = 640
altura_desejada = 480
novo_video_path = diminuir_resolucao(video_path, largura_desejada, altura_desejada)
print(f"Novo vídeo gravado em {novo_video_path}")
