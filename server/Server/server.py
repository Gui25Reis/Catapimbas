from dataclasses import dataclass
from websockets.typing import Data
import websockets
import asyncio

from typing import List
from Server.Sala import Sala

from Usuario import Usuario


@dataclass
class Conexao:
    usuario: Usuario
    sala: Sala


class Servidor:
    def __init__(self) -> None:
        self.conectados: List[Conexao] = []

    @property
    def qtd_conectados(self) -> int:
        return len(self.conectados)

    async def conecta(self, websocket, path) -> None:
        usuario = Usuario(self, websocket)

        if not self.verifica_usuario(usuario):
            nova_conexao = Conexao(usuario, None)
            self.conectados.append(nova_conexao)
    
            print(f"Novo usuário conectado({websocket.remote_address[0]} {websocket.remote_address[1]}). Total: {self.qtd_conectados}")
        await usuario.gerencia()


    def verifica_usuario(self, novo_usuario: Usuario) -> bool:
        for u in self.conectados:
            if u.usuario == novo_usuario:
                return True
        return False


    def desconecta(self, usuario) -> None:
        if usuario in self.conectados:
            self.conectados.remove(usuario)
        print(f"Cliente {usuario.nome} desconectado. Total: {self.qtd_conectados}")


    def verifica_nome(self, nome) -> bool:
        for u in self.conectados:
            if u.usuario.nome == nome:
                return False
        return True


    def cria_sala(self, conexao: Conexao) -> None:
        nova_sala = Sala()
        nova_sala.novo_jogador(conexao.usuario)

        conexao.sala = nova_sala


    def entra_sala(self, codigo: str, conexao: Conexao) -> None:
        sala = self.verifica_codigo(codigo)
        if sala == None:
            # Envia uma mensagem para o usuario falando que deu erro
            pass
        else:
            conexao.sala = sala
            sala.novo_jogador(conexao.usuario)

    def verifica_codigo(self, codigo: str) -> Sala:
        for c in self.conectados:
            if c.sala.get_idSala() == codigo:
                return c.sala
        return None






def main() -> None:
    servidor = Servidor()
    loop = asyncio.get_event_loop()

    start_server = websockets.serve(servidor.conecta, 'localhost', 7890)

    loop.run_until_complete(start_server)
    loop.run_forever()


if __name__ == "__main__":
    main()
