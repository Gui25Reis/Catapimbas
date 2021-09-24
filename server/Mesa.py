from Carta import Carta
from typing import List

class Mesa:

    def __init__(self, cartas: List[Carta], vira: Carta) -> None:
        self.cartas: List[Carta] = cartas
        self.vira: Carta = vira

    def ganhador(self) -> int:
        maior = self.carta_mais_forte()

    def carta_mais_forte(self) -> Carta:
        # Para cada carta na mesa, faça:
        # 