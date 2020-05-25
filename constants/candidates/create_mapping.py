"""Contains constants related to candidate mapping."""

import settings as _settings

import db_nomenclature as _db_nomenclature


ELASTIC_SEARCH_END_POINT = _settings.ELASTIC_SEARCH_ENDPOINT_URL

CANDIDATES_MAPPING = _db_nomenclature.CANDIDATE_MAPPING

API_END_POINT_TO_CREATE_INDEX = f"{ELASTIC_SEARCH_END_POINT}/{CANDIDATES_MAPPING}"

API_END_POINT_TO_CREATE_MAPPING = f"{ELASTIC_SEARCH_END_POINT}/{CANDIDATES_MAPPING}/_mapping"