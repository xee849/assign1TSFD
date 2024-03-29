from timeseries import logger
from timeseries.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from timeseries.pipeline.stage_02_data_prepration import DataPreprocessingPipeline
from timeseries.pipeline.stage_03_model_prepratio import ModelPrepration
STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME}  completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data preprocessing"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<")
    obj=DataPreprocessingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME}  completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Prepration"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<")
    obj=ModelPrepration()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME}  completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e