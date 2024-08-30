# Ruta del video y carpeta de salida
from frame_extractor import extract_frames_ffmpeg
from ultralytics import YOLO

def train_yolo():
    # Create a new YOLO model from scratch
    model = YOLO("yolov8n.yaml")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data="/home/luciano/Documentos/helmet_detection/helmetDetection/config.yaml", epochs=100, imgsz=640, workers=0)

    # Export the model to ONNX format
    success = model.export(format="onnx")

def test_yolo():
    model = YOLO("/home/luciano/Documentos/helmet_detection/helmetDetection/codigo-fran/runs/detect/train7/weights/best.pt")
    results = model.predict(source="/home/luciano/Documentos/helmet_detection/helmetDetection/data/videos/005.mp4", show=True, save=True, save_dir="output")



train_yolo()
