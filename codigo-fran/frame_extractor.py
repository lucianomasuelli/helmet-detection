import subprocess
import os

def extract_frames_ffmpeg(video_path, output_folder):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construir el comando de ffmpeg
    command = [
        'ffmpeg',
        '-i', video_path,             # Archivo de entrada
        os.path.join(output_folder, 'temp_frame_%06d.jpg')  # Patrón de salida temporal
    ]

    # Ejecutar el comando
    subprocess.run(command, check=True)

    # Renombrar archivos para comenzar desde frame_000000.jpg
    for i, filename in enumerate(sorted(os.listdir(output_folder))):
        if filename.startswith('temp_frame_'):
            new_filename = f'frame_{i:06d}.jpg'
            os.rename(
                os.path.join(output_folder, filename),
                os.path.join(output_folder, new_filename)
            )

