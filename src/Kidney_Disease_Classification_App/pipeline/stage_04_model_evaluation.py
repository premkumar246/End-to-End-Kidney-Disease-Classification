from Kidney_Disease_Classification_App.config.configuration import ConfigurationManager
from Kidney_Disease_Classification_App.components.model_evaluation import Evaluation
from Kidney_Disease_Classification_App import logger


STAGE_NAME = "Evaluation"

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.save_score()
        # evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f'*************************')
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 



