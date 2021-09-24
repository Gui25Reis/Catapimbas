from Mesa import Mesa
from Carta import Carta
from typing import List
from Jogador import Jogador
from Baralho import Baralho
from random import shuffle

def main():
    baralho: Baralho = Baralho()

    jogadores: List[Jogador] = []
    for _ in range(4):
        j: Jogador = Jogador(3, [])
        jogadores.append(j)

    shuffle(baralho.cartas)

    # Distribuir cartas
    for i in range(4):
        mao: List[Carta] = []
        for j in range(3):
            carta = baralho.cartas.pop()
            carta.jogador = i
            mao.append(carta)
        jogadores[i].cartas = mao

    vira = baralho.cartas.pop()

    mesa = Mesa([], vira)

    for i in range(len(baralho.cartas)):
        print(f"{baralho.cartas[i].num}{baralho.cartas[i].naipe}", end=" ")

    print()
    print()

    for i in range(4):
        print(f"Jogador {i}:")
        for j in range(3):
            print(f"{jogadores[i].cartas[j].num}{jogadores[i].cartas[j].naipe}", end=" ")
        print()
        print()

    for i in range(3):
        print("Mesa:")
        for j in range(len(jogadores)):
            escolha = int(input())
            mesa.append(jogadores[j].cartas[escolha])
            print(f"{mesa.cartas[j].num}{mesa.cartas[j].naipe}")
        print()
        print("Vira:")
        print(f"{mesa.vira.num}{mesa.vira.naipe}")
        ganhador(mesa.cartas, mesa.vira)
        print()
        print("Ganhador:")
        print()

if __name__ == "__main__":
    main()