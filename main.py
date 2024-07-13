from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeling
from Kidney_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"<<<<<<stage {STAGE_NAME} started >>>>>>>>>")
    obj = DataIngestionTrainingPipeling()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "Prepare base Model"

try:
    logger.info(">>>>>>>>>preparemodeltraining start<<<<<<<")
    logger.info(f">>>>stage {STAGE_NAME} started")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    raise e

        
    
    