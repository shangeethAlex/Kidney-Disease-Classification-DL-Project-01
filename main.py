from Kidney_Disease_Classifier import logger
from Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeling

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"<<<<<<stage {STAGE_NAME} started >>>>>>>>>")
    obj = DataIngestionTrainingPipeling()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<")
except Exception as e:
    raise e
    
    