import datetime

def seconds_to_time(seconds):
    hours = seconds // 3600  # Integer number of hours
    remaining_seconds = seconds % 3600  # Seconds remaining after hours

    minutes = remaining_seconds // 60  # Integer number of minutes
    final_seconds = remaining_seconds % 60  # Seconds remaining after minutes

    # Extract milliseconds
    milliseconds = round((final_seconds - int(final_seconds)) * 1000)

    time = datetime.time(int(hours), int(minutes), int(final_seconds), int(milliseconds * 1000))

    return time

# calcular o tempo que cada deteccao esteve no video
def video_detection_time(frames_counter, video_fps):
    if frames_counter is not None:
        detection_time = {}
        
        for id, qtde_frames in frames_counter.items():
            seconds = qtde_frames / video_fps
            detection_time[id] = seconds_to_time(seconds)
            
        return detection_time
    
# imprime o tempo de todas as deteccoes
def print_formatted_time(time_dict):
    for identifier, time in time_dict.items():
        formatted_time = time.strftime("%H:%M:%S.%f")[:-3]  # Formata o tempo como "hh:mm:ss.mmm"
        print(formatted_time)