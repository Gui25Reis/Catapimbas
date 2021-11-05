from typing import List
from dataclasses import dataclass
from cliente import Cliente

@dataclass
class Jogador:
    cliente: Cliente
    posicao: int


class Sala:
    def __init__(self, codigo_sala: str) -> None:
        self.codigo: str = codigo_sala

        self.jogadores: List[Jogador] = []
        self.host: Jogador = None

        self.jogadores_ativos: int = 0
        self.jogadores_mortos: int = 0
        self.jogo_iniciado: bool = False

    def get_total_jogadores(self) -> int:
        return len(self.jogadores)

    def set_host(self, jogador: Jogador) -> None:
        self.host = jogador

    def novo_jogador(self, cliente: Cliente) -> None:
        jogador = Jogador(cliente, self.get_total_jogadores())
        self.jogadores.append(jogador)







        



