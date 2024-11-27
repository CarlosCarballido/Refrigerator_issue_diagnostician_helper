from fridge.door import Door
from fridge.compressor import Compressor
from fridge.cooling_system import CoolingSystem
from fridge.electrical_system import ElectricalSystem
from fridge.dirt import Dirt
from fridge.refrigerant import Refrigerant
from fridge.fan import Fan

class Refrigerator:
    def __init__(self):
        self.door = Door()
        self.compressor = Compressor()
        self.cooling_system = CoolingSystem()
        self.electrical_system = ElectricalSystem()
        self.dirt = Dirt()
        self.refrigerant = Refrigerant()
        self.fan = Fan()

    def is_door_closed(self) -> bool:
        return self.door.check_seals()

    def is_compressor_working(self) -> bool:
        return self.compressor.check_noise() and self.compressor.check_pressure()

    def is_temperature_adequate(self) -> bool:
        return self.cooling_system.check_temperature()

    def is_voltage_adequate(self) -> bool:
        return self.electrical_system.check_supply()

    def is_clean(self) -> bool:
        return not self.dirt.check_dirt()

    def is_refrigerant_pressure_adequate(self) -> bool:
        return self.refrigerant.check_pressure()

    def is_fan_speed_adequate(self) -> bool:
        return self.fan.check_speed()
