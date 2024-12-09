class Compressor:
    def __init__(self):
        self.noise_level = 0
        self.pressure = 0 

    def check_noise(self) -> bool:
        """
        Verifica si el nivel de ruido del compresor está dentro del rango aceptable.
        """
        acceptable_noise_level = 50
        return self.noise_level <= acceptable_noise_level

    def check_pressure(self) -> bool:
        """
        Verifica si la presión del compresor está en un rango óptimo.
        """
        optimal_pressure_range = (20, 50)
        return optimal_pressure_range[0] <= self.pressure <= optimal_pressure_range[1]

    def set_noise_level(self, noise: int):
        """
        Establece el nivel de ruido del compresor.
        """
        self.noise_level = noise

    def set_pressure(self, pressure: int):
        """
        Establece la presión del compresor.
        """
        self.pressure = pressure
