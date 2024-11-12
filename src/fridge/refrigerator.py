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
        # Implementación para verificar si la puerta está cerrada
        pass

    def is_compressor_working(self) -> bool:
        # Implementación para verificar si el compresor funciona
        pass

    def is_temperature_adequate(self) -> bool:
        # Implementación para verificar si la temperatura es adecuada
        pass

    def is_voltage_adequate(self) -> bool:
        # Implementación para verificar si el voltaje es adecuado
        pass

    def is_clean(self) -> bool:
        # Implementación para verificar si el sistema está limpio
        pass

    def is_sensor_working(self) -> bool:
        # Implementación para verificar si el sensor funciona
        pass

    def is_refrigerant_pressure_adequate(self) -> bool:
        # Implementación para verificar si la presión del refrigerante es adecuada
        pass

    def is_fan_speed_adequate(self) -> bool:
        # Implementación para verificar si la velocidad del ventilador es adecuada
        pass
