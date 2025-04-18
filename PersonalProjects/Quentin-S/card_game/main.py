

class Symbol():
    def __init__(self, deck_size):
    
        formes = ["♥", "♦", "♣", "♠"]
        self.icon: str = formes[deck_size % 4]

        if self.icon == "♥" or self.icon == "♦":
            self.color = "Red"
        else:
            self.color = "Black"

    def __str__(self) -> str:
        return f"{self.icon} ({self.color})"

class Card(Symbol):
    def __init__(self, deck_size):
        super().__init__(deck_size)
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.value: str = numbers[deck_size % 13]
        self.name = self.value + self.icon

    def __str__(self):
        return self.name

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

import random

class Player():
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#--------------------------- GTP CODE ----------------------------

    def play(self):

        if len(self.cards) < 1:
            print(f"{self.name} has no cards left!")
            return None

        print("Your hand:")
        
        for index, card in enumerate(self.cards):
            if (index + 1) % 10 == 0:
                print(f"Card {index:02d}: {card}")

            else: 
                print(f"Card {index:02d}: {card}", end="   ")

        played = False
        while played == False:
            try:
                print("")
                choice = int(input(f"{self.name}, choose a card by entering its index: "))
                played_card = self.cards.pop(choice)
                played = True
            except (ValueError, IndexError):
                pass

        self.history.append(played_card)
        self.turn_count += 1
        print(f"{self.name} turn {self.turn_count} played: {played_card}")
        print("")
        return played_card
    
    def __str__(self) -> str:
        return self.name

#----------------------- GPT CODE --------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

class Deck():
    def __init__(self):
        self.cards = []

    def fill_deck(self, players): 
        deck_size = 12 - 12 % len(players) ## don't generate useless cards
        for i in range(deck_size): ## 3 players = 51 instead of 52 cards
            card = Card(i)
            self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, players):
        while len(self.cards) > 0:
            for player in players:
                card = self.cards.pop(0)
                player.cards.append(card)

#----------------------- GPT CODE --------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

class Board():
    def __init__(self, player_list):
        self.players = [Player(name) for name in player_list]
        self.deck = Deck()
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = [] # played cards

    def start_game(self):
        self.deck.fill_deck(self.players)
        self.deck.shuffle()
        self.deck.distribute(self.players)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#--------------------------- GTP CODE ----------------------------

        # Play turns until all players have no cards left
        while any(player.cards for player in self.players):

            self.turn_count += 1
            print(f"\nTurn {self.turn_count}:")
            
            self.active_cards = []

            for player in self.players:
                if len(player.cards) > 0:
                    played_card = player.play()
                    self.active_cards.append(played_card)
                    self.history_cards.append(played_card)

            print(f"Active cards: {[str(card) for card in self.active_cards]}") # str(card) <-> card.name
            print(f"Total played cards: {len(self.history_cards)}")

#----------------------- GPT CODE --------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

def main():
    player_list = ["Alice", "Bob", "Charlie"]
    ## ask to enter a pseudo: input = class player
    ## append player to board value
    ## create new player

    game = Board(player_list)
    game.start_game()
    
main()
