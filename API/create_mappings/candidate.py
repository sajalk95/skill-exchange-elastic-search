import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from Mappings.candidate import MAPPINGS
from constants.candidates.create_mapping import CANDIDATES_MAPPING, ELASTIC_SEARCH_END_POINT
from settings import USERNAME, PASSWORD, PORT

client = Elasticsearch(
        ELASTIC_SEARCH_END_POINT,
        http_auth=(USERNAME, PASSWORD),
        port=PORT,
    )

INDEX = CANDIDATES_MAPPING
OPERATION_TYPE = 'index'

def create_index():
    client.indices.create(
        index=INDEX,
        body=MAPPINGS
    )

if __name__ == "__main__":
    create_index()