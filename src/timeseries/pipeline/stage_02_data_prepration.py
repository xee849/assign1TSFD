from timeseries.config.configuration import DataConfigrationManager
from timeseries.components.prepare_data import PrepareDataset
from timeseries import logger



STAGE_NAME = "Dataset_preprocessing"


class DataPreprocessingPipeline:
    
    
    def __init__(self):
        pass
    
    
    def main(self):
        config=DataConfigrationManager()
        Prepare_data=config.prepare_data()
        dataset= PrepareDataset(Prepare_data)
        Xt,Yt,xT,yT = dataset.dataset_prepration()
        print(Xt.shape,xT.shape)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<")
        obj=DataPreprocessingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME}  completed <<<<<<\n\n")



    except Exception as e:
        logger.exception(e)
        raise e
