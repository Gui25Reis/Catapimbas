from typing import List
from Carta import Carta

class Jogador:

    def __init__(self, vidas: int, cartas: List[Carta]) -> None:
        self.vidas: int = vidas
        self.cartas: List[Carta] = cartas.copy()
