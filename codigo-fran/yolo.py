from ultralytics import YOLO

def train_yolo():
    # Create a new YOLO model from scratch
    model = YOLO("yolov8n.yaml")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data="config.yaml", epochs=100, imgsz=640)

    # Export the model to ONNX format
    success = model.export(format="onnx")

