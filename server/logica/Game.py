from typing import Dict, List

from Card import Card

class Game:
    def __init__(self, vira: Card):
        self.vira: Card = vira
        self.cards: List[Card] = []
        self.manilhas: List[Card] = []

        self.num_order: List[str] = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
        self.num_order.append(self.num_order.pop((self.num_order.index(self.vira.num)+1)%10))
        self.suit_order: List[str] = ["♦", "♠", "♥", "♣"]
        self.manilha_num: int = self.num_order[len(self.num_order)-1]
        self.meladas: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set_up(self, vira: Card):
        self.vira: Card = vira
        self.cards: List[Card] = []
        self.manilhas: List[Card] = []

        self.num_order: List[str] = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
        self.num_order.append(self.num_order.pop((self.num_order.index(self.vira.num)+1)%10))
        self.suit_order: List[str] = ["♦", "♠", "♥", "♣"]
        self.manilha_num: int = self.num_order[len(self.num_order)-1]
        self.meladas: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def clear(self):
        self.cards = []
        self.manilhas = []
        self.meladas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def push_card(self, card: Card):
        is_highest = True
        if card.num == self.manilha_num:
            for i in range(len(self.manilhas)):
                if self.suit_order.index(card.suit) < self.suit_order.index(self.manilhas[i].suit):
                    self.manilhas.insert(i, card)
                    is_highest = False
                    break
            if is_highest:
                self.manilhas.append(card)
        else:
            for i in range(len(self.cards)):
                if self.num_order.index(card.num) < self.num_order.index(self.cards[i].num):
                    self.cards.insert(i, card)
                    is_highest = False
                    break
            if is_highest:
                self.cards.append(card)
        self.meladas[self.num_order.index(card.num)] += 1

    def highest_card(self) -> Card:
        if len(self.manilhas) > 0:
            return self.manilhas[len(self.manilhas)-1]
        for i in range(len(self.cards)-1, -1, -1):
            if self.meladas[self.num_order.index(self.cards[i].num)] == 1:
                return self.cards[i]
