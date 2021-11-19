class Card:
    def __init__(self, num: int, suit: int) -> None:
        self.num: str = ""
        self.suit: str = ""
        self.player: int = -1

        if num == 0:
            self.num = "A"
        elif num == 10:
            self.num = "J"
        elif num == 11:
            self.num = "Q"
        elif num == 12:
            self.num = "K"
        else:
            self.num = str(num+1)

        if suit == 0:
            self.suit = "♦"
        elif suit == 1:
            self.suit = "♠"
        elif suit == 2:
            self.suit = "♥"
        elif suit == 3:
            self.suit = "♣"
