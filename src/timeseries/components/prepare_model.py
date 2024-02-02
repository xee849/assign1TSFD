
import tensorflow as tf
import os
from timeseries.entity.config_entity import PrepareModel
from keras.models import Sequential
import keras
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.layers import Dense,Dropout
from keras.layers import LSTM
from timeseries import logger




class TSmodel:
    def __init__(self,config :PrepareModel ):
        self.config = config
    
    def get_model(self):
        try:
            look_back = self.config.look_back
            loss_ty = self.config.loss_type
            model = Sequential()
            model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(look_back, 1)))
            model.add(LSTM(50, activation='relu', return_sequences=True))
            model.add(LSTM(50, activation='sigmoid', return_sequences=False))
            model.add(Dense(50))
            model.add(Dropout(0.2))
            model.add(Dense(1))
            model.compile(optimizer='adam', loss=loss_ty)
            model.summary()
            return model
        except Exception as e:
            raise e

        
    
    def save_mod(self,model : keras.Model):
        try:
            os.makedirs(self.config.model_direct,exist_ok=True)
            path=self.config.model_direct
            model.save_weights(path/"lstm.h5")
            logger.info(f"model has been created at {path}")
        except Exception as e:
            raise e

        