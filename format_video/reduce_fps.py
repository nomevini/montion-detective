import cv2

import os
import cv2

def alterar_taxa_frames(video_path, taxa_frames_desejada):
    if not os.path.exists(video_path):
        raise FileNotFoundError("Arquivo de vídeo não encontrado")

    video = cv2.VideoCapture(video_path)

    # verificar a taxa de frames do vídeo original
    taxa_frames_original = video.get(cv2.CAP_PROP_FPS)

    # verificar se a taxa de frames desejada é menor ou igual à taxa de frames do vídeo original
    if taxa_frames_desejada > taxa_frames_original:
        raise ValueError("Taxa de frames desejada é maior que a taxa de frames do vídeo original")

    # obter a largura e altura do vídeo original
    largura = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # criar um objeto VideoWriter para gravar o novo vídeo
    novo_video_path = f"novo_{taxa_frames_desejada}_{video_path}"
    codec = cv2.VideoWriter_fourcc(*'mp4v') # usar codec MP4V para gravar o novo vídeo
    novo_video = cv2.VideoWriter(novo_video_path, codec, taxa_frames_desejada, (largura, altura))

    # calcular quantos frames pular a cada iteração
    taxa_frames_pular = round(taxa_frames_original / taxa_frames_desejada)

    # ler cada frame do vídeo original e gravar o novo vídeo com a taxa de frames desejada
    contador_frames = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        contador_frames += 1
        if contador_frames % taxa_frames_pular == 0:
            novo_video.write(frame)

    # liberar os recursos utilizados
    video.release()
    novo_video.release()
    cv2.destroyAllWindows()

    return novo_video_path

video_path = "640x480_pedestrian_cut.mp4"
taxa_frames_desejada = 6
novo_video_path = alterar_taxa_frames(video_path, taxa_frames_desejada)
print(f"Novo vídeo gravado em {novo_video_path}")
