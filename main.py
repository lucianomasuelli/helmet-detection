# Ruta a tus archivos
from utils.yolo_formatter import convert_yolo_annotations, convert_to_yolo_format
from ultralytics import YOLO

annotations_path = "train_mini/gt.txt"
videos_path = "train_mini/videos"
output_dir = "/"
frames_folder = "train_mini/images/train"
annotations_folder = "train_mini/labels/train"


#convert_to_yolo_format(videos_path, frames_folder, annotations_path, annotations_folder, convert_annotations=False)

def train_yolo():
    # Create a new YOLO model from scratch
    model = YOLO("yolov8n.yaml")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data="config.yaml", epochs=100, imgsz=640, workers=0)

    # Export the model to ONNX format
    success = model.export(format="onnx")

def test_yolo():
    model = YOLO("C:/Users/User/PycharmProjects/yolov8/runs/detect/train7/weights/best.pt")
    results = model.predict(source="videos/008.mp4", show=True, save=True, save_dir="output")

train_yolo()

