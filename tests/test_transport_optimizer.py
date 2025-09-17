from src.services.transport_optimizer import TransportOptimizer
from src.models.enums import AreaType, TransportMode


def test_transport_rules():
    t = TransportOptimizer()
    assert t.select_mode(AreaType.URBAN, 30, None) == TransportMode.WALK
    assert t.select_mode(AreaType.RURAL, 30, None) == TransportMode.DRIVE
    assert t.select_mode(AreaType.MOUNTAIN, 30, None) == TransportMode.HIKE
    assert t.select_mode(AreaType.URBAN, 75, None) == TransportMode.TRANSIT
    assert t.select_mode(AreaType.RURAL, 40, True) == TransportMode.TRANSIT


