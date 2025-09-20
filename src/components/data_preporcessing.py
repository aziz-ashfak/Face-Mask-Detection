import os 
import sys
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import xml.etree.ElementTree as ET
from shutil import copy,move
from PIL import Image
from glob import glob
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.components.data_load import load_dataset
from src.constant import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.utils.common import read_yaml,create_directories
from src.logger  import  logging
from src.exception import CustomException

class Data_Preprocessing :
    def __init__(self):
        load_dataset()
    def extract_information(self):
        xml_file_path = glob('artifacts/data_ingestion/Face_Musk_Detection/Datatset/annotations/*.xml')

        data_label = dict(filename = [],width = [],height=[],xmin = [],xmax = [],ymin = [],ymax = [],name = [])

        for file in xml_file_path:
            tree = ET.parse(file)
            root = tree.getroot()
            filename = root.find('filename').text
            size = root.find('size')
            width = float(size.find('width').text)
            height = float(size.find('height').text)
            object_all = root.findall('object')
            for obj in object_all:
                name = obj.find('name').text
                bndbox = obj.find('bndbox')
                xmin = float(bndbox.find('xmin').text)
                xmax = float(bndbox.find('xmax').text)
                ymin = float(bndbox.find('ymin').text)
                ymax = float(bndbox.find('ymax').text)
                data_label['filename'].append(filename)
                data_label['width'].append(width)
                data_label['height'].append(height)
                data_label['xmin'].append(xmin)
                data_label['xmax'].append(xmax)
                data_label['ymin'].append(ymin)
                data_label['ymax'].append(ymax)
                data_label['name'].append(name)
                
        df = pd.DataFrame(data_label)
        # center_x,cencter_y,width,height
        df['center_x'] = (df['xmin'] + df['xmax'])/(2 * df['width'])
        df['center_y'] = (df['ymin'] + df['ymax'])/(2 * df['height'])
        df['W'] = (df['xmax'] - df['xmin'])/(df['width'])
        df['H'] = (df['ymax'] - df['ymin'])/(df['height'])

        soucrce_code = {
            'with_mask':0,
            'without_mask':1,
            'mask_weared_incorrect':2
        }
        df['label'] = df['name'].apply(lambda x: soucrce_code[x])
        cols = ['filename','center_x', 'center_y', 'W', 'H', 'label']
        df = df[cols]
        return df 
    def data_spliter(self):
        df = self.extract_information()
        uniqueFilename = df['filename'].unique()
        fileDf = pd.DataFrame(uniqueFilename,columns=['filename'])
        train_file = tuple(fileDf.sample(frac=0.8,random_state=42)['filename'])
        test_file  = tuple(fileDf.query(f'filename not in {train_file}')['filename'])

        train_df = df.query(f"filename in {train_file}")
        test_df = df.query(f"filename in {test_file}")

        train_groupby = train_df.groupby('filename')
        test_groupby = test_df.groupby('filename')
        return train_groupby,test_groupby
    def pipeline_folder(self):
        train_folder = "artifacts/data_ingestion/YoloDataset/train_set"
        os.makedirs(train_folder,exist_ok=True)
        test_folder = "artifacts/data_ingestion/YoloDataset/test_set"
        os.makedirs(test_folder,exist_ok=True)
        return train_folder,test_folder

    
    