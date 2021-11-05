from typing import List

from Card import Card

class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []
        
        for i in range(4):
            for j in range(13):
                if j not in [7, 8, 9]:
                    card = Card(j, i)
                    self.cards.append(card)
