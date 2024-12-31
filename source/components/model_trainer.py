import os
import sys
import numpy as np 
import pandas as pd
from source.exception import myexception
from source.logger import logging
from source.utils.utils import save_object
from source.utils.utils import evaluate_model
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('Artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config= ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={

                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet(),
                'DecisionTreeRegressor' : DecisionTreeRegressor(),
                'RandomForestRegressor' : RandomForestRegressor(),
                'GradientBoostRegressor' : GradientBoostingRegressor(),
                'AdaBoostRegressor' : AdaBoostRegressor(),
                'KNeighborsRegressor' : KNeighborsRegressor()

            }

            model_report : dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            best_model_score=max(sorted(model_report.values()))
            best_model_name= list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]
            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model

            )

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise myexception(e,sys)

