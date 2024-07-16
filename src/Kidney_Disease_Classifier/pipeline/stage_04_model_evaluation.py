from Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from Kidney_Disease_Classifier.components.model_evaluation_mlflow import Evaluation
from Kidney_Disease_Classifier import logger


STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


          
if __name__ == "__main__":
    try:
        logger.info("---------------------")
        logger.info("----stage{STAGE_NAME} started---------")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"----stage {STAGE_NAME} completed--------")
    except Exception as e:
        logger.exception(e)
        raise e