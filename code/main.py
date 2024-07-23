from ultralytics import YOLO

model = YOLO('yolov8n.yaml') # Load pretrained model

results = model.train(data="config.yaml", epochs=100, imgsz=640)