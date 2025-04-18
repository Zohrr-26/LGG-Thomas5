import random


class Symbol:
    """Class representing a card symbol with an icon and color."""
    def __init__(self, deck_size: int) -> None:
        """
        Initialize the symbol based on a deck index.

        :param deck_size: An integer used to determine the card suit.
        """
        formes = ["♥", "♦", "♣", "♠"]
        self.icon: str = formes[deck_size % 4]
        if self.icon in ["♥", "♦"]:
            self.color: str = "Red"
        else:
            self.color: str = "Black"

    def __str__(self) -> str:
        return f"{self.icon} ({self.color})"


class Card(Symbol):
    """Class representing a playing card with a suit and value."""
    def __init__(self, deck_size: int) -> None:
        """
        Initialize a card with a suit and value based on the deck index.

        :param deck_size: An integer used to determine the card suit and value.
        """
        super().__init__(deck_size)
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.value: str = numbers[deck_size % 13]
        self.name: str = self.value + self.icon

    def __str__(self) -> str:
        return self.name


class Player:
    """Class representing a player in the card game."""
    def __init__(self, name: str) -> None:
        """
        Initialize a player with a name and empty hand.

        :param name: The name of the player.
        """
        self.name: str = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []

    def play(self) -> Card:
        """
        Randomly pick a card from the player's hand, play it, and record it in history.

        :return: The card that was played.
        """
        if not self.cards:
            print(f"{self.name} has no cards left!")
            return None
        played_card: Card = random.choice(self.cards)
        self.cards.remove(played_card)
        self.history.append(played_card)
        self.turn_count += 1
        print(f"{self.name} turn {self.turn_count} played: {played_card}")
        return played_card

    def __str__(self) -> str:
        return self.name


class Deck:
    """Class representing a deck of 52 playing cards."""
    def __init__(self) -> None:
        """
        Initialize an empty deck.
        """
        self.cards: list[Card] = []

    def fill_deck(self) -> None:
        """
        Fill the deck with 52 unique cards.
        """
        for i in range(52):
            card = Card(i)
            self.cards.append(card)

    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)

    def distribute(self, players: list[Player]) -> None:
        """
        Distribute the cards evenly among the players.

        :param players: List of Player objects.
        """
        while self.cards:
            for player in players:
                if self.cards:
                    card = self.cards.pop(0)
                    player.cards.append(card)


class Board:
    """Class representing the game board which manages players and game turns."""
    def __init__(self, player_list: list[str]) -> None:
        """
        Initialize the board with a list of player names and a deck.

        :param player_list: List of player names.
        """
        self.players: list[Player] = [Player(name) for name in player_list]
        self.deck: Deck = Deck()
        self.turn_count: int = 0
        self.active_cards: list[Card] = []  # Last card played by each player in the current turn
        self.history_cards: list[Card] = []  # All cards played during the game

    def start_game(self) -> None:
        """
        Start the game by filling, shuffling, and distributing the deck, then running game turns until players have no cards left.
        """
        self.deck.fill_deck()
        self.deck.shuffle()
        self.deck.distribute(self.players)

        # Play turns until all players have no cards left
        while any(player.cards for player in self.players):
            self.turn_count += 1
            print(f"\nTurn {self.turn_count}:")
            self.active_cards = []
            for player in self.players:
                if player.cards:
                    played_card = player.play()
                    if played_card is not None:
                        self.active_cards.append(played_card)
                        self.history_cards.append(played_card)
            print(f"Active cards: {[str(card) for card in self.active_cards]}")
            print(f"Total played cards: {len(self.history_cards)}")


class Game:
    """Class representing the overall card game."""
    def __init__(self, player_list: list[str]) -> None:
        """
        Initialize the game with a list of players.

        :param player_list: List of player names.
        """
        self.board: Board = Board(player_list)

    def play(self) -> None:
        """
        Start the game.
        """
        self.board.start_game()


def main() -> None:
    """
    Main function to start the card game.
    """
    player_list = ["Alice", "Bob", "Charlie"]
    game = Game(player_list)
    game.play()


if __name__ == "__main__":
    main()