from ultralytics import YOLO
import cv2

modelPath = "/home/luciano/Documentos/helmet_detection/helmetDetection/code/runs/detect/train2/weights/best.pt" # Load pretrained model
model = YOLO(modelPath)

source = "/home/luciano/Documentos/helmet_detection/helmetDetection/data/videos/001.mp4"
cap = cv2.VideoCapture(source)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()