import sys
setattr(sys.modules[__name__], '__path__', '__path__')

import tqdm
import bcrypt
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from Data.jobs.data_dev import DATA
from Mappings.job import MAPPINGS
from constants.jobs.create_mapping import JOBS_MAPPING, ELASTIC_SEARCH_END_POINT
from settings import USERNAME, PASSWORD, PORT, pwhash

def generate_actions(operationType, index):
    for doc in DATA:
        Id = doc['id']
        doc['applied'] = []
        doc['shortlisted'] = []
        doc['interviewScheduled'] = []
        doc['interviewCompleted'] = []
        doc['selected'] = []
        doc['rejected'] = []
        doc['offerReleased'] = []
        doc['candidateJoined'] = []
        newDoc = {
            '_op_type': operationType,
            '_index': index,
            '_id': Id,
            '_source': doc
        }
        yield newDoc

client = Elasticsearch(
    ELASTIC_SEARCH_END_POINT,
    http_auth=(USERNAME, PASSWORD),
    port=PORT,
)

INDEX = JOBS_MAPPING
OPERATION_TYPE = 'index'

def create_index():
    client.indices.create(
        index=INDEX,
        body=MAPPINGS
    )

def main():
    number_of_docs = len(DATA)

    if (client.indices.exists(index=INDEX) == False):
        create_index()

    progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=client, index=INDEX, actions=generate_actions(operationType=OPERATION_TYPE, index=INDEX),
    ):
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, number_of_docs))


if __name__ == "__main__":
    password = input("Enter the password: ")
    password = password.encode("utf-8")
    if bcrypt.checkpw(password, pwhash):
        main()
    else:
        print("Password didn't match")