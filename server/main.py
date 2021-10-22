from Mesa import Mesa
from Carta import Carta
from typing import List
from Jogador import Jogador
from Baralho import Baralho
from random import shuffle

def main():
    # Cria o baralho
    baralho: Baralho = Baralho()

    # Define os jogadores da mesa
    jogadores: List[Jogador] = []
    for _ in range(4):
        j: Jogador = Jogador(3, [])
        jogadores.append(j)

    # Embraralha as cartas
    shuffle(baralho.cartas)

    # Distribuir cartas para os jogadores
    for i in range(len(jogadores)):
        mao: List[Carta] = []
        for j in range(3):
            carta = baralho.cartas.pop()
            carta.jogador = i
            mao.append(carta)
        jogadores[i].cartas = mao

    # Define a vira
    vira = baralho.cartas.pop()

    # Cria a mesa
    mesa = Mesa([], vira)

    # for i in range(len(baralho.cartas)):
    #     print(f"{baralho.cartas[i].num}{baralho.cartas[i].naipe}", end=" ")

    print()
    print()

    # Exibe as cartas de cada jogador
    for i in range(len(jogadores)):
        print(f"Jogador {i}:")
        for j in range(3):
            print(f"{jogadores[i].cartas[j].num}{jogadores[i].cartas[j].naipe}", end=" ")
        print()
        print()

    # Inicia as rodadas
    for i in range(3):
        print("Mesa")
        print()
        print("Vira: ", end="")
        print(f"{mesa.vira.num}{mesa.vira.naipe}")
        print()
        # Turnos
        print("Cartas jogadas:")
        for j in range(len(jogadores)):
            print(f"Jogador {j}: ", end="")
            escolha = int(input())
            while escolha < 0 or escolha > 2-i:
                print("Carta inválida! Tente novamente: ", end="")
                escolha = int(input())
            mesa.cartas.append(jogadores[j].cartas.pop(escolha))
            print(f"Jogador {j}: {mesa.cartas[j].num}{mesa.cartas[j].naipe}\n")
        print()
        print("Ganhador:")
        ganhador: int = mesa.ganhador()
        print(f"Jogador {ganhador}: {mesa.cartas[ganhador].num}{mesa.cartas[ganhador].naipe}")
        print()
        mesa.cartas.clear()
        jogadores.append(jogadores.pop())

if __name__ == "__main__":
    main()