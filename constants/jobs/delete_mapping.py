"""Contains constants related to candidate mapping."""

import settings as _settings

import db_nomenclature as _db_nomenclature


ELASTIC_SEARCH_END_POINT = _settings.ELASTIC_SEARCH_ENDPOINT_URL

JOB_MAPPING = _db_nomenclature.JOB_MAPPING

API_END_POINT_TO_DELETE_MAPPING = f"{ELASTIC_SEARCH_END_POINT}/{JOB_MAPPING}"