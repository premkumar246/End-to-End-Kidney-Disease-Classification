from Kidney_Disease_Classification_App import logger 
from Kidney_Disease_Classification_App.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Kidney_Disease_Classification_App.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Kidney_Disease_Classification_App.pipeline.stage_03_model_training import ModelTrainingPipeline
from Kidney_Disease_Classification_App.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage :: {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>> stage :: {STAGE_NAME} completed <<<<<<< \n\n x========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>>>> stage :: {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage :: {STAGE_NAME} completed <<<<<<< \n\n x========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>>> stage :: {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage :: {STAGE_NAME} completed <<<<<<< \n\n x========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model_Evaluation"
try:
    logger.info(f'*************************')
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e 
