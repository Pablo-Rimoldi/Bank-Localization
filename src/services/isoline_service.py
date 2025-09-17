from typing import Dict, Any

import requests

from src.models.enums import TransportMode
from src.utils.config import settings


class IsolineService:
    def compute_minutes_by_context(self, area_type: str) -> int:
        if area_type == "urban":
            return 20
        if area_type == "rural":
            return 30
        return 45

    def build_isoline(self, lat: float, lon: float, minutes: int, mode: TransportMode) -> Dict[str, Any]:
        params = {
            "lat": lat,
            "lon": lon,
            "type": "time",
            "mode": mode.value,
            "range": minutes * 60,
            "apiKey": settings.geoapify_api_key,
        }
        resp = requests.get(settings.isoline_endpoint, params=params, timeout=settings.http_timeout_seconds)
        resp.raise_for_status()
        return resp.json()


