from typing import Dict
import websockets
import asyncio
import json


URL:str = "ws://127.0.0.1:7890"

connection = None

async def listen() -> None:
    global connection

    input("Aperte qualquer coisa para conectar.")
    
    async with websockets.connect(URL) as ws:
        connection = ws

        msg_incial: Dict[str,str] = criar_sala()
        await ws.send(json.dumps(msg_incial))

        msg = await connection.recv()
        print(msg)

        while True:
            msg_input = input("\nMensagem: ")
            await ws.send(msg_input)


def criar_sala() -> Dict[str,str]:
    nome = str(input("\n\nDigite seu nome: "))
    qtd_jogadores = int(input("Quantidade de jogadores: "))
    qtd_vidas = int(input("Quantidade de vidas: "))

    return {
        "nome" : nome,
        "jogadores" : qtd_jogadores,
        "vidas" : qtd_vidas
    }


async def recebe_mensagem() -> None:
    while True:
        msg = await connection.recv()
        print(f"Server: {msg}")

asyncio.get_event_loop().run_until_complete(listen())