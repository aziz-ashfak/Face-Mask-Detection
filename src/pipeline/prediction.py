from ultralytics import YOLO
import cv2 
import matplotlib.pyplot as plt



def make_prediction(img_path):

    model_path = 'best_model/best.onnx'

    model = YOLO(model_path)

    results = model.predict(img_path)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    for result in results:
            plotted_img = result.plot()
            plt.figure(figsize=(8, 6))  
            plt.imshow(plotted_img)    
            plt.axis('off')             
            plt.show() 
