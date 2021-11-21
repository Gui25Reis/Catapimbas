from typing import List

from Card import Card

class Player:
    def __init__(self, lifes: int) -> None:
        self.lifes: int = lifes
        self.current_points: int = 0
        self.target_points: int = 0
        self.cards: List[Card] = []

    def add_point(self):
        self.current_points += 1

    def update_lifes(self):
        self.lifes -= abs(self.target_points - self.current_points)
        self.points = 0
