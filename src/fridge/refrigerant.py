class Refrigerant:
    def __init__(self):
        self.pressure = 0
        self.has_leak = False

    def check_pressure(self) -> bool:
        """
        Verifica si la presión del refrigerante está dentro del rango óptimo.
        """
        optimal_pressure_range = (30, 60)
        return optimal_pressure_range[0] <= self.pressure <= optimal_pressure_range[1]

    def check_leaks(self) -> bool:
        """
        Verifica si hay fugas en el sistema de refrigerante.
        """
        return self.has_leak

    def set_pressure(self, pressure: int):
        """
        Establece la presión del refrigerante.
        """
        self.pressure = pressure
        print(f"Presión del refrigerante ajustada a {self.pressure} PSI")

    def simulate_leak(self):
        """
        Simula una fuga en el sistema de refrigerante.
        """
        self.has_leak = True
        print("Se ha detectado una fuga en el sistema de refrigerante.")

    def repair_leak(self):
        """
        Repara las fugas en el sistema de refrigerante.
        """
        self.has_leak = False
        print("La fuga en el sistema de refrigerante ha sido reparada.")
