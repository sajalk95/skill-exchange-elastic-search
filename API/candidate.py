import tqdm
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from Data.candidates.data_dev import DATA
from Mappings.candidate import MAPPINGS
from constants.candidates.create_mapping import CANDIDATES_MAPPING, ELASTIC_SEARCH_END_POINT
from settings import USERNAME, PASSWORD, PORT

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


INDEX = CANDIDATES_MAPPING
OPERATION_TYPE = 'index'

def create_index():
    client.indices.create(
        index=INDEX,
        body=MAPPINGS
    )

def delete_index():
    client.indices.delete(index=INDEX)

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
    main()
