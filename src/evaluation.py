import logging
import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import mean_squared_error, r2_score

class Evaluation(ABC):
    """abstract class for evaluation"""
    @abstractmethod
    def calculate_score(self, y_true: np.array, y_pred: np.ndarray):
        """calculates scores for the model"""


class MSE(Evaluation):
    """evaluation strategy that used MSE"""
    def calculate_score(self, y_true: np.array, y_pred: np.ndarray):
        """calculate scores"""
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse

        except Exception as e:
            logging.error(f"Error in calculating MSE: {e}")
            raise e

class R2(Evaluation):
    """evaluation strategy that used R2"""
    def calculate_score(self, y_true: np.array, y_pred: np.ndarray):
        """calculate scores"""
        try:
            logging.info("Calculating R2")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2: {}".format(r2))
            return r2

        except Exception as e:
            logging.error(f"Error in calculating R2: {e}")
            raise e

class RMSE(Evaluation):
    """evaluation strategy that used RMSE"""
    def calculate_score(self, y_true: np.array, y_pred: np.ndarray):
        """calculate scores"""
        try:
            logging.info("Calculating RMSE")
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))
            logging.info("RMSE: {}".format(rmse))
            return rmse

        except Exception as e:
            logging.error(f"Error in calculating RMSE: {e}")
            raise e
