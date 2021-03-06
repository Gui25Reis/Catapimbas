from typing import List
from random import shuffle

from Card import Card
from Deck import Deck
from Player import Player
from Game import Game

def main():
    num_players = int(input("Quantidade de jogadores: "))
    num_lifes = int(input("Quatidade de vidas para cada jogador: "))
    max_hand = int(39/num_players)
    num_hand = 1
    is_increasing = True
    accumulated_meladas = 0

    players: List[Player] = []
    for _ in range(num_players):
        player = Player(num_lifes)
        players.append(player)

    while len(players) > 1:
        deck = Deck()
        shuffle(deck.cards)
        for i in range(len(players)):
            hand: List[Card] = []
            for _ in range(num_hand):
                card = deck.cards.pop()
                card.player = i
                hand.append(card)
            players[i].cards = hand.copy()

        # Define a vira
        vira: Card = deck.cards.pop()
        game = Game(vira)

        print(f"\nVira: {game.vira.num}{game.vira.suit}\n")

        # Exibe as cartas de cada jogador
        for i in range(len(players)):
            print(f"JOGADOR {i}")
            print(f"Vidas: {players[i].lifes}")
            print(f"Cartas: ", end="")
            for j in range(num_hand):
                print(f"{players[i].cards[j].num}{players[i].cards[j].suit}", end=" ")
            print("\n")

        # Pontos de cada jogador
        for i in range(len(players)):
            players[i].target_points = int(input(f"Quantos pontos o JOGADOR {i} fará?: "))
        print()

        for i in range(len(players)):
            print(f"JOGADOR {i}")
            print(f"Pontos: {players[i].target_points}\n")

        # Inicia as rodadas
        for i in range(num_hand):
            # Turnos
            print("Cartas jogadas:")
            for j in range(len(players)):
                print(f"Jogador {j}: ", end="")
                opt: int = int(input())
                while opt < 0 or opt > num_hand-1-i:
                    print("Carta inválida! Tente novamente: ", end="")
                    opt: int = int(input())
                game.push_card(players[j].cards.pop(opt))
            print("\nGanhador:")
            highest_card: Card = game.highest_card()
            if highest_card is None:
                accumulated_meladas += 1
                print("MELOU TUDO!")
            else:
                if accumulated_meladas > 0:
                    for i in range(accumulated_meladas):
                        players[highest_card.player].add_point()
                else:
                    players[highest_card.player].add_point()
                print(f"Jogador {highest_card.player}: {highest_card.num}{highest_card.suit}")
            game.clear()
            players.append(players.pop())

        for player in players:
            player.update_lifes()
        
        if is_increasing:
            num_hand += 1
            if num_hand+1 > max_hand:
                is_increasing = False
        else:
            num_hand -= 1
            if num_hand-1 < 1:
                is_increasing = True

if __name__ == "__main__":
    main()
