import logging

import pandas as pd
from zenml import step

class IngestData:
    def __init__(self, data_path: str):
        """init method"""
        self.path = data_path

    def get_data(self):
        """reading data from data_path"""
        logging.info(f"Reading data from: {self.path}")
        return pd.read_csv(self.path)

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """ingest data from data_path"""
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error in reading data: {e}")
        raise e
