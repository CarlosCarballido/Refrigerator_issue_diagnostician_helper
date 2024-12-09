class Door:
    def __init__(self):
        self.is_closed = True
        self.seal_condition = 100

    def check_seals(self) -> bool:
        """
        Verifica si los sellos de la puerta están en condiciones adecuadas.
        """
        seal_threshold = 75
        return self.seal_condition >= seal_threshold

    def open_door(self):
        """
        Abre la puerta de la nevera.
        """
        self.is_closed = False
        print("La puerta está abierta.")

    def close_door(self):
        """
        Cierra la puerta de la nevera.
        """
        self.is_closed = True
        print("La puerta está cerrada.")

    def is_door_closed(self) -> bool:
        """
        Verifica si la puerta está cerrada.
        """
        return self.is_closed

    def deteriorate_seals(self, amount: int):
        """
        Deteriora los sellos de la puerta por una cantidad específica.
        """
        self.seal_condition = max(0, self.seal_condition - amount)
        print(f"Condición del sello: {self.seal_condition}")

    def repair_seals(self):
        """
        Repara los sellos de la puerta restaurando su condición al máximo.
        """
        self.seal_condition = 100
        print("Los sellos de la puerta han sido reparados.")
