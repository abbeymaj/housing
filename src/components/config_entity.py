# Importing packages
import os
from dataclasses import dataclass


# Creating a class to store the path to the raw dataset
@dataclass
class DatasetPathConfig:
    raw_data_path: str = 'https://github.com/abbeymaj80/my-ml-datasets/blob/master/project_datasets/housing/housing.csv'