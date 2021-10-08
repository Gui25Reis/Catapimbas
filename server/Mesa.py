from Carta import Carta
from typing import List

class Mesa:

    def __init__(self, cartas: List[Carta], vira: Carta) -> None:
        self.cartas: List[Carta] = cartas
        self.vira: Carta = vira

    def ganhador(self) -> int:
        maior_carta = self.carta_mais_forte()
        return self.cartas.index(maior_carta)

    def carta_mais_forte(self) -> Carta:
        ordem_forca_num: List[str] = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
        ordem_forca_naipe: List[str] = ["♦", "♠", "♥", "♣"]

        ordem_forca_num.append(ordem_forca_num.pop((ordem_forca_num.index(self.vira.num)+1)%10))
        manilha_num: int = ordem_forca_num[len(ordem_forca_num)-1]

        cartas_ordenadas: List[Carta] = []
        cartas_meladas: List[Carta] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        cartas_ordenadas.append(self.cartas[0])

        for i in range(1, len(self.cartas)):
            carta_atual = self.cartas[i]
            cartas_meladas[ordem_forca_num.index(carta_atual.num)] += 1
            eh_maior = True
            for j in range(len(cartas_ordenadas)):
                if ordem_forca_num.index(carta_atual.num) < ordem_forca_num.index(cartas_ordenadas[j].num):
                    cartas_ordenadas.insert(j, carta_atual)
                    eh_maior = False
                    break
            if eh_maior:
                cartas_ordenadas.append(carta_atual)

        tem_manilha = False
        manilhas: List[Carta] = []
        qntd_manilhas = 0
        for i in range(len(cartas_ordenadas)):
            if cartas_ordenadas[i].num == manilha_num:
                tem_manilha = True
                qntd_manilhas += 1
        
        for i in range(qntd_manilhas):
            manilhas.append(cartas_ordenadas.pop())

        for i in range(len(manilhas)):
            manilha_atual: int = 0
            for j in range(1, len(manilhas)):
                if ordem_forca_naipe.index(manilhas[j].naipe) < ordem_forca_naipe.index(manilhas[manilha_atual].naipe):
                    manilha_atual = j
            cartas_ordenadas.append(manilhas.pop(manilha_atual))

        if tem_manilha:
            return cartas_ordenadas.pop()
        else:
            for i in range(len(cartas_ordenadas)-1, -1, -1):
                if cartas_meladas[ordem_forca_num.index(cartas_ordenadas[i].num)] == 1:
                    return cartas_ordenadas[i]
