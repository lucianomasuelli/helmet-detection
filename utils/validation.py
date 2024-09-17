import os
import shutil
import random

def split_data(image_folder, label_folder, train_image_folder, val_image_folder, train_label_folder, val_label_folder, val_ratio=0.2):
    # Crear las carpetas de destino si no existen
    os.makedirs(train_image_folder, exist_ok=True)
    os.makedirs(val_image_folder, exist_ok=True)
    os.makedirs(train_label_folder, exist_ok=True)
    os.makedirs(val_label_folder, exist_ok=True)

    # Obtener lista de archivos de imagen y etiquetas, ignorando archivos ocultos y otros no válidos
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png')) and not f.startswith('.')])
    label_files = sorted([f for f in os.listdir(label_folder) if f.endswith('.txt') and not f.startswith('.')])

    # Crear un conjunto con los nombres de las etiquetas (sin extensiones)
    label_names = set(os.path.splitext(f)[0] for f in label_files)

    # Filtrar solo las imágenes que tienen una etiqueta correspondiente
    paired_files = [(img, os.path.splitext(img)[0] + '.txt') for img in image_files if os.path.splitext(img)[0] in label_names]

    # Mezclar aleatoriamente los archivos
    random.shuffle(paired_files)

    # Dividir en entrenamiento y validación
    val_size = int(len(paired_files) * val_ratio)
    val_files = paired_files[:val_size]
    train_files = paired_files[val_size:]

    # Copiar los archivos a las carpetas correspondientes
    for image_file, label_file in train_files:
        shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_image_folder, image_file))
        shutil.copy(os.path.join(label_folder, label_file), os.path.join(train_label_folder, label_file))

    for image_file, label_file in val_files:
        shutil.copy(os.path.join(image_folder, image_file), os.path.join(val_image_folder, image_file))
        shutil.copy(os.path.join(label_folder, label_file), os.path.join(val_label_folder, label_file))

    print(f"División completada: {len(train_files)} en entrenamiento, {len(val_files)} en validación.")

