class ElectricalSystem:
    def __init__(self):
        self.voltage = 220  # Voltaje inicial del sistema (en voltios)
        self.status = True  # Estado del suministro eléctrico (True: funcional, False: fallo)

    def check_supply(self) -> bool:
        """
        Verifica si el suministro eléctrico es adecuado.
        """
        optimal_voltage_range = (200, 240)  # Rango aceptable de voltaje (en voltios)
        return self.status and optimal_voltage_range[0] <= self.voltage <= optimal_voltage_range[1]

    def set_voltage(self, voltage: int):
        """
        Establece el voltaje actual del sistema eléctrico.
        """
        self.voltage = voltage
        print(f"Voltaje actualizado a {self.voltage} V")

    def power_outage(self):
        """
        Simula un fallo en el suministro eléctrico.
        """
        self.status = False
        print("Fallo en el suministro eléctrico.")

    def restore_power(self):
        """
        Restaura el suministro eléctrico.
        """
        self.status = True
        print("Suministro eléctrico restaurado.")
