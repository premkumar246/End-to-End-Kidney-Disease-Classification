from Kidney_Disease_Classification_App import logger 
from Kidney_Disease_Classification_App.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage :: {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>> stage :: {STAGE_NAME} completed <<<<<<< \n\n x========x")
except Exception as e:
    logger.exception(e)
    raise e
