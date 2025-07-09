from network_security.constant.training_pipeline import SAVE_MODEL_DIR,MODEL_FILE_NAME
import os
import sys
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor, model):
        try:
            self.model = model
            self.preprocessor = preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    def predict(self,x):
        try:
            x_transformed = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transformed)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
