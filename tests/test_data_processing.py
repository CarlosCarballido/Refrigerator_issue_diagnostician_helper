import pytest
from src.simulation import introduce_random_failure
from src.fridge.refrigerator import Refrigerator

@pytest.fixture
def setup_fridge():
    """
    Fixture para inicializar un objeto Refrigerator.
    """
    return Refrigerator()

def test_introduce_random_failure(setup_fridge):
    """
    Prueba que introduce_random_failure afecta a al menos un componente de la nevera.
    """
    fridge = setup_fridge
    introduce_random_failure(fridge)

    components = [
        fridge.door.seals_worn,
        fridge.compressor.noise_level,
        fridge.cooling_system.temperature,
        fridge.electrical_system.voltage,
        fridge.dirt.level,
        fridge.refrigerant.leak,
        fridge.fan.speed
    ]

    assert any(comp > 0 for comp in components), "No failure was introduced."
