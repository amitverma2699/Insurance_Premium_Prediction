import os 
import sys
import numpy as np
import pandas as pd
from source.exception import myexception
from source.logger import logging
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from source.utils.utils import save_object


@dataclass

class DataTransformationConfig:
    preprocessor_file_path=os.path.join("Artifacts","preprocessor.pkl")


class DataTransformation():
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation(self):

        try:
            logging.info("Data Transformation initiated")

            categorical_cols=['sex','smoker','region']
            numerical_cols=['age','bmi','children']

            sex_categories=['male','female']
            smoker_categories=['no','yes']
            region_categories=['southwest', 'southeast', 'northwest', 'northeast']

            logging.info("Pipeline initiated")

            num_pipeline=Pipeline(
                steps=[
                    ('Imputer', SimpleImputer(strategy='median')),
                    ('Scaler',StandardScaler())
                ]
            )


            cat_pipeline=Pipeline(
                steps=[
                    ('Imputer',SimpleImputer(strategy='most_frequent')),
                    ('Ordinalencoder',OrdinalEncoder(categories=[sex_categories,smoker_categories,region_categories])),
                    ('StandardScaler',StandardScaler())

                ]
            )


            preprocessor=ColumnTransformer([
                ('Num_pipeline',num_pipeline,numerical_cols),
                ('Cat_pipeline',cat_pipeline,categorical_cols)
            ])

            return preprocessor

        except Exception as e:
            logging.info("Exception occured in the get_data_transformation ")
            raise myexception(e,sys)
        


    def initiate_data_transformation(self,train_path,test_path):
        try:

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data")
            logging.info(f"Train dataframe head : \n{train_df.head().to_string()}")
            logging.info(f"Train dataframe head : \n{train_df.head().to_string()}")

            preprocessing_obj=self.get_data_transformation()

            target_column_name='expenses'
            drop_column =[target_column_name]

            input_feature_train_data=train_df.drop(columns=drop_column,axis=1)
            target_feature_train_data=train_df[target_column_name]

            input_feature_test_data=test_df.drop(columns=drop_column,axis=1)
            target_feature_test_data=test_df[target_column_name]

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_data)

            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_data)

            logging.info("Applying preprocessing object on training and testing datasets.")

            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_data)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_data)]



            save_object(
                file_path=self.data_transformation_config.preprocessor_file_path,
                obj=preprocessing_obj
            )


            logging.info("Preprocessed pickle file saved")

            return (

                train_arr,
                test_arr
            )
        except Exception as e:
            logging.info("Exception occured in the initiate_data_tranformation")
            raise myexception(e,sys)