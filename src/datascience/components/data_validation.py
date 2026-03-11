import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            valiation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    valiation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {valiation_status}")
                else:
                    valiation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {valiation_status}")

            return valiation_status

        except Exception as e:
            raise e