import numpy as np
import pandas as pd
from source.exception import myexception
from source.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
from pathlib import Path
import os
import sys

class DataIngestionConfig:
    raw_data_path : str =os.path.join("Artifacts","raw.csv")
    train_data_path : str =os.path.join("Artifacts","train.csv")
    test_data_path : str =os.path.join("Artifacts","test.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Start")

        try:

            data=pd.read_csv(Path(os.path.join("notebooks/data","insurance.csv")))
            logging.info("Dataset is Loaded")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Save the raw data in artifacts folder")

            logging.info("Perform train test split")
            train_data,test_data=train_test_split(data,test_size=0.2)

            logging.info("train_test_split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion part complete")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
            raise myexception(e,sys)
