from typing import List
from Carta import Carta

class Baralho:

    def __init__(self) -> None:
        self.cartas: List[Carta] = []
        
        for i in range(4):
            for j in range(13):
                if j not in [7, 8, 9]:
                    carta = Carta(j, i)
                    self.cartas.append(carta)