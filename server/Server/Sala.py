from typing import List
from dataclasses import dataclass
from Usuario import Usuario

@dataclass
class Jogador:
    cliente: Usuario
    posicao: int


class Sala:
    def __init__(self) -> None:
        self.codigo: str = ""

        self.jogadores: List[Jogador] = []
        self.host: Jogador = None

        self.jogadores_ativos: int = 0
        self.jogadores_mortos: int = 0
        self.jogo_iniciado: bool = False

    def get_total_jogadores(self) -> int:
        return len(self.jogadores)

    def get_idSala(self) -> str:
        if not self.codigo: 
            self.codigo = self.gerar_codigo()
        return self.codigo

    def set_host(self, jogador: Jogador) -> None:
        self.host = jogador

    def novo_jogador(self, cliente: Usuario) -> None:
        # Precisa mandar um evento para o jogador conectado + jogadores que ja foram conectados.
        jogador = Jogador(cliente, self.get_total_jogadores())
        self.jogadores.append(jogador)
    
    def gerar_codigo(self) -> str:
        return "gui25"

    def verificar_entrada(self, qtd_jogadores: int, qtd_vidas: int) -> True:
        return True if 0 < qtd_jogadores <= 10 and 1 < qtd_vidas < 5 else False







        



