from timeseries import logger
from timeseries.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME}  completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e