class Carta:

    def __init__(self, num: int, naipe: int) -> None:
        self.num: str = ""
        self.naipe: str = ""
        self.jogador: int = -1

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

        if naipe == 0:
            self.naipe = "♦"
        elif naipe == 1:
            self.naipe = "♠"
        elif naipe == 2:
            self.naipe = "♥"
        elif naipe == 3:
            self.naipe = "♣"