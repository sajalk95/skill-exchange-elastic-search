"""Contains constants related to location mapping."""

import settings as _settings

import db_nomenclature as _db_nomenclature


ELASTIC_SEARCH_END_POINT = _settings.ELASTIC_SEARCH_ENDPOINT_URL

LOCATION_MAPPING = _db_nomenclature.LOCATION_MAPPING

API_END_POINT_TO_DELETE_MAPPING = f"{ELASTIC_SEARCH_END_POINT}/{LOCATION_MAPPING}"