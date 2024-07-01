from Kidney_Disease_Classification_App.config.configuration import ConfigurationManager
from Kidney_Disease_Classification_App.components.prepare_base_model import PrepareBaseModel
from Kidney_Disease_Classification_App import logger


STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()