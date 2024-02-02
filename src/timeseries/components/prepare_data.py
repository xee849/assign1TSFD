from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from timeseries import logger
from timeseries.utils.common import create_dataset,transform
from timeseries.entity.config_entity import PrepareDataConfig






class PrepareDataset:
    def __init__(self,config : PrepareDataConfig):
        self.config = config
    

    def dataset_prepration(self):
        try:
            datasetpath=self.config.data_path
            column_name = self.config.coll_name
            train_Size=self.config.train_size
            look_back=self.config.look_Back
            df = pd.read_excel(datasetpath ,engine='openpyxl')
            logger.info(f"file load successfuly from the path {datasetpath}")
            df.Date = pd.to_datetime(df.Date)
            df = df.set_index("Date")
            dataset = df.filter([column_name])
            dataset=transform(dataset)
            train_size = int(len(dataset) * train_Size)
            test_size = len(dataset) - train_size
            train = dataset[0:train_size,:]
            test = dataset[train_size:len(dataset),:]
            Train_X,trainY = create_dataset(train,look_back)
            Test_X,testY = create_dataset(test,look_back)
            trainX = np.reshape(Train_X, (Train_X.shape[0], Train_X.shape[1], 1))
            testX = np.reshape(Test_X, (Test_X.shape[0], Test_X.shape[1], 1))
            logger.info(f"Dataset training shape is {trainX.shape} and test shape is {testX.shape}")

            return trainX,trainY,testX,testY
        except Exception as e:
            raise e

        


        