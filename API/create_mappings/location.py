import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from Data.location.data_dev import DATA
from Mappings.location import MAPPINGS
from settings import USERNAME, PASSWORD, PORT
from constants.locations.create_mapping import ELASTIC_SEARCH_END_POINT, LOCATION_MAPPING

client = Elasticsearch(
        ELASTIC_SEARCH_END_POINT,
        http_auth=(USERNAME, PASSWORD),
        port=PORT,
    )

INDEX = LOCATION_MAPPING
OPERATION_TYPE = 'index'

def create_index():
    client.indices.create(
        index=INDEX,
        body=MAPPINGS
    )

if __name__ == "__main__":
    create_index()