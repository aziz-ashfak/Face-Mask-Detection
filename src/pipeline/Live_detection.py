from ultralytics import YOLO
import cv2
import time 
import math


cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("best_model/best.onnx")
 
classNames = ['with_mask', 'without_mask', 'mask_weared_incorrect']
 
prev_frame_time = 0
new_frame_time = 0
 
while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)
     
    for result in results:
            plotted_img = result.plot()
             
            cv2.imshow("Image",plotted_img)    
            cv2.waitKey(1)
 
 
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)
    cv2.imshow("Image",img) 
    cv2.waitKey(1)