import sys
from source.logger import logging
from source.exception import myexception
from source.components.data_ingestion import DataIngestion
from source.components.data_transformation import DataTransformation
from source.components.model_trainer import ModelTrainer
import pandas as pd


obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr,test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

model_trainer_obj=ModelTrainer()

model_trainer_obj.initiate_model_training(train_arr,test_arr)