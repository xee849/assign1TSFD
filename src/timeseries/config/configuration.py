from timeseries.constants import *
from timeseries.utils.common import read_yaml,create_directories
from timeseries.entity.config_entity import DataIngestionConfig,PrepareDataConfig,PrepareModel

class ConfigrationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_file=config.local_data_file)
        return data_ingestion_config


    def prepare_data(self)->PrepareDataConfig:
        config=self.config.prepare_data
        prepare_base_model_config = PrepareDataConfig(data_path=Path(config.data_path),train_size=self.params.TRAIN_SIZE,
                                                      coll_name=config.col_name,look_Back=self.params.LOOK_BACK)
        return prepare_base_model_config
    
    def prepare_model_config(self)->PrepareModel:
        config=self.config.prepare_model
        create_directories([config.model_directory])
        pre_model=PrepareModel(model_direct=Path(config.model_directory),loss_type=config.error_type,Batch_size=self.params.BATCH_SIZE,epochs=self.params.EPOCHS,
                               look_back=self.params.LOOK_BACK)
        return pre_model
