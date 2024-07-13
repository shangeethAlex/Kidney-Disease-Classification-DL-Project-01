from Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from Kidney_Disease_Classifier.components.prepare_base_model import PrepareBaseModel
from Kidney_Disease_Classifier import logger


STAGE_NAME = "Prepare base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
    
if __name__ == "__main__":
    
    try:
        logger.info(">>>>>>>>>preparemodeltraining start<<<<<<<")
        logger.info(f">>>>stage {STAGE_NAME} started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<stage {STAGE_NAME} completed >>>>>>")
        
    except Exception as e:
        logger.exception(e)
        raise e