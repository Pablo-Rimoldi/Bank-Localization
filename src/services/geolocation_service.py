from typing import Tuple, Optional

import requests

from src.models.enums import AreaType
from src.utils.config import settings


class GeolocationService:
    def geocode(self, address: str) -> Optional[Tuple[float, float]]:
        params = {
            "text": address,
            "apiKey": settings.geoapify_api_key,
        }
        resp = requests.get(settings.geocode_endpoint,
                            params=params, timeout=settings.http_timeout_seconds)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        if not features:
            return None
        coords = features[0]["geometry"]["coordinates"]
        return coords[1], coords[0]

    def detect_area_type(self, population_density_per_km2: Optional[float], elevation_meters: Optional[float]) -> AreaType:
        if elevation_meters is not None and elevation_meters > 500:
            return AreaType.MOUNTAIN
        if population_density_per_km2 is not None and population_density_per_km2 > 1500:
            return AreaType.URBAN
        return AreaType.RURAL
