import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import bcrypt
from elasticsearch import Elasticsearch
from Mappings.job import MAPPINGS
from constants.jobs.create_mapping import JOBS_MAPPING, ELASTIC_SEARCH_END_POINT
from settings import USERNAME, PASSWORD, PORT, pwhash

client = Elasticsearch(
        ELASTIC_SEARCH_END_POINT,
        http_auth=(USERNAME, PASSWORD),
        port=PORT,
    )

INDEX = JOBS_MAPPING
OPERATION_TYPE = 'index'

def delete_index():
    password = input("Enter the password: ")
    password = password.encode("utf-8")
    if bcrypt.checkpw(password, pwhash):
        client.indices.delete(index=INDEX)
    else:
        print("Password didn't match")

if __name__ == "__main__":
    delete_index()
