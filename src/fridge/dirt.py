class Dirt:
    def __init__(self):
        self.dirt_level = 0

    def check_dirt(self) -> bool:
        """
        Verifica si el nivel de suciedad supera un umbral aceptable.
        """
        dirt_threshold = 50
        return self.dirt_level > dirt_threshold

    def clean(self):
        """
        Limpia el sistema reduciendo el nivel de suciedad a 0.
        """
        self.dirt_level = 0
        print("El sistema ha sido limpiado.")

    def accumulate_dirt(self, amount: int):
        """
        Incrementa el nivel de suciedad por una cantidad específica.
        """
        self.dirt_level = min(100, self.dirt_level + amount)
        print(f"Suciedad acumulada: {self.dirt_level}")

    def get_dirt_level(self) -> int:
        """
        Retorna el nivel actual de suciedad.
        """
        return self.dirt_level
