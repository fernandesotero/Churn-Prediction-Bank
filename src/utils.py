'''
Script aims to provide util functions to be used in components and pipeline
'''

'''
Importing the libraries.
'''

# File handling.
import os
import pickle

# Debugging and verbose.
import sys
from src.exception import CustomException

# Data manipulation.
import pandas as pd
import numpy as np

def save_object(file_path, object):

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_object:
            pickle.dump(object, file_object)

    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):

    try:
        with open(file_path, 'rb') as file_object:
            return pickle.load(file_object)
    
    except Exception as e:
        raise CustomException(e, sys)
