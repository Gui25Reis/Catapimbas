from typing import List
from random import shuffle, triangular

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

    game = Game()

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

        # Cria a mesa

        print()
        print()

        # Exibe as cartas de cada jogador
        for i in range(len(players)):
            print(f"Jogador {i}:")
            for j in range(num_hand):
                print(f"{players[i].cards[j].num}{players[i].cards[j].suit}", end=" ")
            print()
            print()

        # Inicia as rodadas
        for i in range(num_hand):
            print("Vira: ", end="")
            print(f"{game.vira.num}{game.vira.suit}")
            print()
            # Turnos
            print("Cartas jogadas:")
            for j in range(len(players)):
                print(f"Jogador {j}: ", end="")
                opt: int = int(input())
                while opt < 0 or opt > num_hand-1-i:
                    print("Carta inválida! Tente novamente: ", end="")
                    opt: int = int(input())
                game.push_card(players[j].cards.pop(opt))
                # print(f"Jogador {j}: {game.cards[j].num}{game.cards[j].suit}\n")
            print()
            print("Ganhador:")
            highest_card: Card = game.highest_card()
            players[highest_card.player].add_point()
            print(f"Jogador {highest_card.player}: {highest_card.num}{highest_card.suit}")
            print()
            game.clear()
            players.append(players.pop())
        
        game.reset()

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
