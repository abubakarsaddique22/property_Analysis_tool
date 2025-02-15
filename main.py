from src.mlproject.exception import CustomException
# from src.mlproject.logger import logging
from src.mlproject.logger import logging

import os 
import sys 

def test_exc():
    try:
        logging.info("The execution has started")
        1/0
    except Exception as e:
        raise CustomException(e,sys)

if __name__ =='__main__':
    try:
        test_exc()
    except Exception as e:
        print(e)


