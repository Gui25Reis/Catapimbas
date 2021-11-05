import websockets
import asyncio

PORT = 7890

clients_connected:set = set()

print(f"Ligando server na porta {PORT}")

async def echo(websocket, path) -> None:
    print("Novo cliente entrou")

    clients_connected.add(websocket)

    print(len(clients_connected))
    while True:
        async for msg in websocket:
            print(f"Mensagem recebida: {msg}")
            cont = 0
            for client in clients_connected:
                cont += 1
                print(cont)
                await client.send(f"Msg: {msg}")

    

# Criando o server
start_server = websockets.serve(echo, "localhost", PORT)

# Liga ele 
asyncio.get_event_loop().run_until_complete(start_server)

# Deia rodando
asyncio.get_event_loop().run_forever()