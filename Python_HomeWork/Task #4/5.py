class CardDeck:
    def __init__(self):
        self.suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.values = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        self.cards = [
            (value + " " + suit) for suit in self.suits for value in self.values
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        else:
            card = self.cards[self.index]
            self.index += 1
            return card


deck = CardDeck()
for card in deck:
    print(card)
