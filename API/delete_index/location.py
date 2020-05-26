import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import bcrypt
from elasticsearch import Elasticsearch
from Mappings.location import MAPPINGS
from settings import USERNAME, PASSWORD, PORT, pwhash
from constants.locations.create_mapping import ELASTIC_SEARCH_END_POINT, LOCATION_MAPPING

client = Elasticsearch(
        ELASTIC_SEARCH_END_POINT,
        http_auth=(USERNAME, PASSWORD),
        port=PORT,
    )

INDEX = LOCATION_MAPPING
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
