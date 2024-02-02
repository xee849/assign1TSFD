import urllib.request as ur
import os
from timeseries import logger
from timeseries.utils.common import get_size
from timeseries.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config
    

    def download_file(self) -> str:

        try:
            dataset_url=self.config.source_URL
            download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok =True)
            #logger.info(f"download datarom {dataset_url} into file {download_dir}")
            file_id=dataset_url
            file_name=file_id.rsplit('/')[-1]
            ur.urlretrieve(file_id,os.path.join(download_dir,file_name))
            logger.info(f"download datarom {dataset_url} into file {download_dir}")
        except Exception as e:
            raise e
