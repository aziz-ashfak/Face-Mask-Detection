import os
import sys
import numpy as np 
import pandas as pd
import tensorflow as tf  
from shutil import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))
from src.components.data_preporcessing import Data_Preprocessing
from src.logger import logging
from src.exception import CustomException
class DataIngestion:
    def __init__(self):
        pass
    # save data 
    def save_data(self,filename,folder,groupBy):
        
        image_path  = os.path.join('artifacts/data_ingestion/Face_Musk_Detection/Datatset/images',filename)
        
        dist_image_path = os.path.join(folder,filename)
        copy(image_path,dist_image_path)
        
        text_path = os.path.join(folder,
                                os.path.splitext(filename)[0] + '.txt')
        groupBy.get_group(filename).set_index('filename').to_csv(text_path,header=False,
                                                                index=False,sep=' ')
    def data_preparation(self):
        try:
            data_preprocesses = Data_Preprocessing()
            train_groupby,test_groupby = data_preprocesses.data_spliter()
            train_folder,test_folder = data_preprocesses.pipeline_folder()

            train_series = pd.Series(train_groupby.groups.keys())
            train_series.apply(self.save_data,args=(train_folder,train_groupby))

            test_series = pd.Series(test_groupby.groups.keys())
            test_series.apply(self.save_data,args=(test_folder,test_groupby))
        except Exception as e:
            
            raise CustomException(e,sys)

if __name__ == '__main__' :
    data_ingestion = DataIngestion()
    data_ingestion.data_preparation()