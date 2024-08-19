import os
import subprocess


def extract_frames_ffmpeg(video_path, output_folder, video_id):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construir el comando de ffmpeg
    command = [
        'ffmpeg',
        '-i', video_path,  # Archivo de entrada
        os.path.join(output_folder, 'temp_frame_%06d.jpg')  # Patrón de salida temporal
    ]

    # Ejecutar el comando
    subprocess.run(command, check=True)

    # Renombrar archivos para que sigan el formato video_<video_id>_frame_<frame_number>.jpg
    for i, filename in enumerate(sorted(os.listdir(output_folder))):
        if filename.startswith('temp_frame_'):
            frame_number = i + 1  # Comenzar la numeración de los images desde 1
            new_filename = f'video_{video_id}_frame_{frame_number}.jpg'
            os.rename(
                os.path.join(output_folder, filename),
                os.path.join(output_folder, new_filename)
            )


def convert_yolo_annotations(annotations_path, annotations_folder):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(annotations_folder):
        os.makedirs(annotations_folder)

    with open(annotations_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        video_id, frame, bb_left, bb_top, bb_width, bb_height, class_id = map(int, line.split(','))

        # Nombre del archivo basado en video_id y frame
        frame_filename = f'video_{video_id}_frame_{frame}.jpg'
        annotation_filename = f'video_{video_id}_frame_{frame}.txt'

        # Verificar si existe el archivo, y en caso de que exista agregar la linea

        if not os.path.exists(os.path.join(annotations_folder, annotation_filename)):
            with open(os.path.join(annotations_folder, annotation_filename), 'w') as file:
                file.write(
                    f'{class_id - 1} {bb_left} {bb_top} {bb_width} {bb_height}\n'
                )
        else:
            with open(os.path.join(annotations_folder, annotation_filename), 'a') as file:
                file.write(
                    f'{class_id - 1} {bb_left} {bb_top} {bb_width} {bb_height}\n'
                )


def convert_to_yolo_format(videos_path, frames_folder, annotations_path, annotations_folder, extract_frames=True, convert_annotations=True):
    # Recorrer todos los videos en la carpeta
    if(extract_frames):
        for video_id, video_filename in enumerate(sorted(os.listdir(videos_path))):
            video_id += 1
            video_path = os.path.join(videos_path, video_filename)
            extract_frames_ffmpeg(video_path, frames_folder, video_id)
    if(convert_annotations):
        convert_yolo_annotations(annotations_path, annotations_folder)