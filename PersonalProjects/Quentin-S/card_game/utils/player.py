
from card import Card
import random

class Player(Card):
    def __init__(self):
        self.cards = [] ## cards = Card()

        self.turn_count = 0
        self.number_of_cards = 0
        self.history = [] ## old Card() ## Card() the player already used

    def play(self):
        

        return ## Card() played
