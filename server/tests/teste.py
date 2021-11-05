# class Classe01:
#     def func_01(self):
#         print("Estou na classe 01")
#         pass
    

# class Classe02(Classe01):
#     def func_01(self):
#         print("Estou na classe 02")
#         super().func_01()
        

# a = Classe02()
# a.func_01()


def mygenerator(n):
   for i in range(1, n, 2):
      yield i**3

gen01 = mygenerator(10)

print("Gen 01 - Loop 01")
for x in gen01:
    print(x)

print("\nGen 01 - Loop 02")
for x in gen01:
    print(x)


gen02 = (i**3 for i in range(1,10,2))

print("\n\nGen 02 - Loop 01")
for x in gen02:
    print(x)

print("\nGen 02 - Loop 02")
for x in gen02:
    print(x)


"""from enum import Enum

class Teste(Enum):
    badUrl = "Url não existe"
    badConnection = "Houve um erro na conexão"


print(Teste.badUrl)
print(Teste.badUrl.name)
print(Teste.badUrl.value)


def some_action() -> None:
    raise Exception(Teste.badUrl.value)
        

def some_action_2() -> None:
    try:
        some_action()
    except Exception as erro:
        print(erro)
    
some_action_2()
"""



"""
import websockets
import asyncio


PORT = 7890

print(f"Ligando server na porta {PORT}")

async def echo(websocket, path) -> None:
    print("Novo cliente entrou")

    async for msg in websocket:
        print(f"Mensagem recebida: {msg}")

        # Espera mandar a mensagem pra poder receber uma nova
        await websocket.send(f"Msg: {msg}")

            


# Criando o server
start_server = websockets.serve(echo, "localhost", PORT)

# Liga ele 
asyncio.get_event_loop().run_until_complete(start_server)

# Deia rodando
asyncio.get_event_loop().run_forever()

"""