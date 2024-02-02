from timeseries.components.prepare_model import TSmodel
from timeseries.config.configuration import ConfigrationManager
from timeseries import logger

STAGE_NAME = "Model prepration"

class ModelPrepration:
    def __init__(self):
        pass

    def main(self):
        config=ConfigrationManager()
        prepare_model_config=config.prepare_model_config()
        tsmodel=TSmodel(config=prepare_model_config)
        modele=tsmodel.get_model()
        tsmodel.save_mod(modele)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME} started <<<<<<")
        obj = ModelPrepration()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    