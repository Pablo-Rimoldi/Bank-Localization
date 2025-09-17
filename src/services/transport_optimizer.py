from typing import Optional

from src.models.enums import AreaType, TransportMode


class TransportOptimizer:
    def select_mode(self, area_type: AreaType, eta: Optional[int], mobilita_ridotta: Optional[bool]) -> TransportMode:
        if mobilita_ridotta:
            return TransportMode.TRANSIT
        if eta is not None and eta >= 70:
            return TransportMode.TRANSIT

        if area_type == AreaType.URBAN:
            return TransportMode.WALK
        if area_type == AreaType.RURAL:
            return TransportMode.DRIVE
        if area_type == AreaType.MOUNTAIN:
            return TransportMode.HIKE

        return TransportMode.WALK
