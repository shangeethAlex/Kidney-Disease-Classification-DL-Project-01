from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeling
from Kidney_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Kidney_Disease_Classifier.pipeline.stage_03_model_training_pipeline import ModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"<<<<<<stage {STAGE_NAME} started >>>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeling()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base Model"

try:
    logger.info(">>>>>>>>>preparemodeltraining start<<<<<<<")
    logger.info(f">>>>stage {STAGE_NAME} started")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"<<<<<<<<<<stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"
          
try:
    logger.info("---------------------")
    logger.info("----stage{STAGE_NAME} started---------")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"----stage {STAGE_NAME} completed--------")
except Exception as e:
    logger.exception(e)
    raise e

        
    
    