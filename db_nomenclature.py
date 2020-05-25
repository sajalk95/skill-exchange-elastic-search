"""Contains all the mapping names and names related to elastic search."""

import settings

DEV_OR_TEST_OR_PROD_OR_LOCALHOST = settings.DEV_OR_TEST_OR_PROD_LOCALHOST.lower()


CANDIDATE_MAPPING = f"candidate_docs_new_{DEV_OR_TEST_OR_PROD_OR_LOCALHOST}"

JOB_MAPPING = f"job_docs_new_{DEV_OR_TEST_OR_PROD_OR_LOCALHOST}"

LOCATION_MAPPING = f"location_docs_new_{DEV_OR_TEST_OR_PROD_OR_LOCALHOST}"

