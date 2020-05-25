import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from Mappings.job import MAPPINGS
from constants.jobs.create_mapping import JOBS_MAPPING, ELASTIC_SEARCH_END_POINT
from settings import USERNAME, PASSWORD, PORT

client = Elasticsearch(
        ELASTIC_SEARCH_END_POINT,
        http_auth=(USERNAME, PASSWORD),
        port=PORT,
    )

INDEX = JOBS_MAPPING
OPERATION_TYPE = 'index'

def delete_index():
    client.indices.delete(index=INDEX)

if __name__ == "__main__":
    delete_index()
