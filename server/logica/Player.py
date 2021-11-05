from typing import List

from Card import Card

class Player:
    def __init__(self, lifes: int) -> None:
        self.lifes: int = lifes
        self.points: int = 0
        self.cards: List[Card] = []

    def add_point(self):
        self.points += 1

    def update_lifes(self):
        self.lifes -= abs(self.points)
        self.points = 0
