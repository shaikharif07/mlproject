# components : a set of modules
#code related to bringing data in from multiple sources will be written here 
#reading data is done here 

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

#dataclass is used to describe variables in a function
@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts',"train.csv")
    test_data_path : str=os.path.join('artifacts',"test.csv")
    raw_data_path : str=os.path.join('artifacts',"data.csv")

    
class DataInjection:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion componen")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Dataset sucessfully read and converted to DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)         
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('train test split initiated')
            train_set,test_set  = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj = DataInjection()
    train_data, test_data = obj.initiate_data_ingestion()

    data_tranformation = DataTransformation()
    train_arr,test_arr, _=data_tranformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))