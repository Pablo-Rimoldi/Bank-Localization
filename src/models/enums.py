from enum import Enum


class TransportMode(str, Enum):
    DRIVE = "drive"
    WALK = "walk"
    TRANSIT = "transit"
    HIKE = "hike"


class AreaType(str, Enum):
    URBAN = "urban"
    RURAL = "rural"
    MOUNTAIN = "mountain"


