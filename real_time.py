from ultralytics import YOLO
import cv2

model = YOLO("yolov8m_custom.pt")

results = model.predict(source="0", conf=0.5, show=True)

print(results)