"""Contains constants related to candidate mapping."""

import settings as _settings

import db_nomenclature as _db_nomenclature


ELASTIC_SEARCH_END_POINT = _settings.ELASTIC_SEARCH_ENDPOINT_URL

CANDIDATE_MAPPING = _db_nomenclature.CANDIDATE_MAPPING

API_END_POINT_TO_DELETE_MAPPING = f"{ELASTIC_SEARCH_END_POINT}/{CANDIDATE_MAPPING}"