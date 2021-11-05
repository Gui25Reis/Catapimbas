from websockets.typing import Data
import websockets
import asyncio

from typing import List

from cliente import Cliente

class Servidor:
    def __init__(self) -> None:
        self.conectados: List[Cliente] = []

    @property
    def qunt_conectados(self) -> int:
        return len(self.conectados)

    async def conecta(self, websocket, path) -> None:
        cliente = Cliente(self, websocket)
        if cliente not in self.conectados:
            self.conectados.append(cliente)
            print(f"Novo cliente conectado({websocket.remote_address[0]} {websocket.remote_address[1]}). Total: {self.qunt_conectados}")
        await cliente.gerencia()


    def desconecta(self, cliente) -> None:
        if cliente in self.conectados:
            self.conectados.remove(cliente)
        print(f"Cliente {cliente.nome} desconectado. Total: {self.qunt_conectados}")


    async def envia_a_todos(self, origem:Cliente, mensagem) -> None:
        for cliente in self.conectados:
            if origem != cliente and cliente.conectado:
                print(f"Enviando de <{origem.nome}> para <{cliente.nome}>: {mensagem}")
                await cliente.envia(f"{origem.nome} >> {mensagem}")


    async def envia_a_destinatario(self, origem, mensagem, destinatario) -> bool:
        for cliente in self.conectados:
            if cliente.nome == destinatario and origem != cliente and cliente.conectado:
                print(f"Enviando de <{origem.nome}> para <{cliente.nome}>: {mensagem}")
                await cliente.envia(f"PRIVADO de {origem.nome} >> {mensagem}")
                return True
        return False


    def verifica_nome(self, nome) -> bool:
        for cliente in self.conectados:
            if cliente.nome and cliente.nome == nome:
                return False
        return True



def main() -> None:
    servidor = Servidor()
    loop = asyncio.get_event_loop()

    start_server = websockets.serve(servidor.conecta, 'localhost', 7890)

    loop.run_until_complete(start_server)
    loop.run_forever()


if __name__ == "__main__":
    main()
