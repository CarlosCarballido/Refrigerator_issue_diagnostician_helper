class CoolingSystem:
    def __init__(self):
        self.temperature = 0  # Temperatura actual del sistema de enfriamiento

    def check_temperature(self) -> bool:
        """
        Verifica si la temperatura del sistema de enfriamiento está dentro del rango óptimo.
        """
        optimal_temperature_range = (-5, 5)  # Rango de temperatura óptima (en °C)
        return optimal_temperature_range[0] <= self.temperature <= optimal_temperature_range[1]

    def set_temperature(self, temperature: float):
        """
        Establece la temperatura actual del sistema de enfriamiento.
        """
        self.temperature = temperature

    def adjust_temperature(self, target_temperature: float):
        """
        Ajusta la temperatura del sistema de enfriamiento hacia una temperatura objetivo.
        """
        if self.temperature < target_temperature:
            self.increase_temperature(target_temperature)
        elif self.temperature > target_temperature:
            self.decrease_temperature(target_temperature)

    def increase_temperature(self, target_temperature: float):
        """
        Incrementa la temperatura gradualmente hacia un valor objetivo.
        """
        while self.temperature < target_temperature:
            self.temperature += 0.5  # Simulación de incremento gradual
            print(f"Aumentando temperatura: {self.temperature} °C")

    def decrease_temperature(self, target_temperature: float):
        """
        Disminuye la temperatura gradualmente hacia un valor objetivo.
        """
        while self.temperature > target_temperature:
            self.temperature -= 0.5  # Simulación de decremento gradual
            print(f"Disminuyendo temperatura: {self.temperature} °C")
