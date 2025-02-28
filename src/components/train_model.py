import pandas as  pd
import numpy as np
import tensorflow as tf
import os 
import sys
from ultralytics  import YOLO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))
from src.logger import logging
from src.exception import  CustomException
from src.components.data_ingestion import DataIngestion

data_ingestion = DataIngestion()
data_ingestion.data_preparation()

model = YOLO(model = "yolo11n.pt")

# make yaml pipeline 

data = """
train : ../artifacts/data_ingestion/YoloDataset/train_set
val :  ../artifacts/data_ingestion/YoloDataset/test_set
nc : 3 
names : [
        'with_mask',
        'mask_weared_incorrect',
        'without_mask'
        ]
"""
with open('data.yaml',mode ='w') as f :
    f.write(data)
    f.close()
    
train_results = model.train(
    data="D:/ObjectDetection(project-1)/data.yaml",  
    epochs=50,  
    imgsz=640,
    batch = 32
)