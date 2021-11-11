from websockets.typing import Data as DataWebsocket
import json

from Server.Sala import Sala


class Usuario:
    def __init__(self, servidor, websocket):
        self.cliente = websocket
        self.servidor = servidor
        self.nome = None

    def __del__(self) -> None:
        self.cliente.close()

    @property
    def conectado(self) -> bool:
        return self.cliente.open
    

    async def gerencia(self):
        try:
            while True:
                mensagem = await self.recebe()
                if mensagem:
                    msg_json = json.loads(mensagem)
                    print(msg_json)
                    await self.processa_comandos(msg_json)

                else:
                    break
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            self.servidor.desconecta(self)


    async def envia(self, mensagem: DataWebsocket) -> None:
        await self.cliente.send(mensagem)


    async def recebe(self) -> DataWebsocket:
        mensagem: DataWebsocket = await self.cliente.recv()
        return mensagem


    async def processa_comandos(self, mensagem) -> None:
        if self.nome:  # Verifica se o usuário já definiu seu nome.
            print(f"{self.nome} < {mensagem}")
            await self.servidor.envia_a_todos(self, mensagem)
        else:
            self.nome = mensagem["nome"]
            await self.envia("Dados recebidos.")




















    async def altera_nome(self, comandos) -> None:
        """Altera o nome do usuário corrente, mas verifica se este é único"""
        if len(comandos) > 1 and self.servidor.verifica_nome(comandos[1]):
            self.nome = comandos[1]
            await self.envia(f"Nome alterado com sucesso para {self.nome}")
        else:
            await self.envia("Nome em uso ou inválido. Escolha um outro.")


    async def apenas_para(self, comandos):
        """Envia a mensagem apenas para um cliente específico"""
        if len(comandos) < 3:
            await self.envia("Comando incorreto. /apenas Destinatário mensagem")
            return
        destinatario = comandos[1]
        mensagem = " ".join(comandos[2:])
        enviado = await self.servidor.envia_a_destinatario(self, mensagem, destinatario)
        if not enviado:
            await self.envia(f"Destinatário {destinatario} não encontrado. Mensagem não enviada.")
