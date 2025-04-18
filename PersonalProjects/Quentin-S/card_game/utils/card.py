
class Symbol():
    def __init__(self):
        self.color = []
        self.icon = ["♥", "♦", "♣", "♠"]

class Card(Symbol):
    def __init__(self):
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
