"""Contains end point related info."""
import pathlib
import os
from os.path import join
from dotenv import load_dotenv
 
dotenv_path = join(pathlib.Path().absolute(), '.env')
load_dotenv(dotenv_path)

DEV_OR_TEST_OR_PROD_LOCALHOST = "DEV"

ELASTIC_SEARCH_ENDPOINT_URL = os.getenv('ELASTIC_SEARCH_ENDPOINT_URL')

username = f'{DEV_OR_TEST_OR_PROD_LOCALHOST}_USERNAME'
password = f'{DEV_OR_TEST_OR_PROD_LOCALHOST}_USER_PASSWORD'

USERNAME = os.getenv(username)
PASSWORD = os.getenv(password)

PORT = os.getenv('PORT')