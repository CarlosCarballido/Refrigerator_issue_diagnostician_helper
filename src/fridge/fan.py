class Fan:
    def __init__(self):
        self.speed = 0

    def check_speed(self) -> bool:
        """
        Verifica si la velocidad del ventilador está dentro del rango óptimo.
        """
        optimal_speed_range = (1000, 3000)
        return optimal_speed_range[0] <= self.speed <= optimal_speed_range[1]

    def set_speed(self, speed: int):
        """
        Establece la velocidad del ventilador.
        """
        self.speed = speed
        print(f"Velocidad del ventilador ajustada a {self.speed} RPM")

    def increase_speed(self, increment: int):
        """
        Incrementa la velocidad del ventilador.
        """
        self.speed += increment
        print(f"Velocidad del ventilador incrementada a {self.speed} RPM")

    def decrease_speed(self, decrement: int):
        """
        Disminuye la velocidad del ventilador.
        """
        self.speed = max(0, self.speed - decrement)
        print(f"Velocidad del ventilador reducida a {self.speed} RPM")
