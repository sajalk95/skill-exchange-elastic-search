"""Contains end point related info."""
import pathlib
import os
from os.path import join
from dotenv import load_dotenv
 
dotenv_path = join(pathlib.Path().absolute(), '.env')
load_dotenv(dotenv_path)

DEV_OR_TEST_OR_PROD_LOCALHOST = "dev"

ELASTIC_SEARCH_ENDPOINT_URL = os.getenv('ELASTIC_SEARCH_ENDPOINT_URL')

USERNAME = os.getenv(f'{DEV_OR_TEST_OR_PROD_LOCALHOST}_USERNAME')
PASSWORD = os.getenv(f'{DEV_OR_TEST_OR_PROD_LOCALHOST}_USER_PASSWORD')

PORT = os.getenv('PORT')