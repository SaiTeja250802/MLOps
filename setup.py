# from setuptools import find_packages, setup

# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Performing MLOps',
#     description='A project on Mlops',
#     author='SaiTeja',
#     license='MIT',
# )

# NOTE: For windows user-
# This file must be created in the root of the project 
# where Training and Prediction batch file as are present

import os
from glob import glob


data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {filePath}")
        os.system(f"dvc add {filePath}")

print("\n #### all files added to dvc ####")