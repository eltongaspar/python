import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        aces = 0
        for card in self.cards:
            if card.rank.isdigit():
                self.value += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                self.value += 10
            else:  # Ace
                aces += 1
                self.value += 11
        while aces > 0 and self.value > 21:
            self.value -= 10
            aces -= 1

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Game setup
deck = Deck()
deck.shuffle()

player_hand = Hand()
player_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())
player_hand.calculate_value()

dealer_hand = Hand()
dealer_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
dealer_hand.calculate_value()

# Game logic
print("Player's hand:", player_hand)
print("Dealer's hand:", dealer_hand.cards[0])

# Player's turn
while True:
    action = input("Do you want to hit or stand? ").lower()
    if action == 'hit':
        player_hand.add_card(deck.deal_card())
        player_hand.calculate_value()
        print("Player's hand:", player_hand)
        if player_hand.value > 21:
            print("Bust! You lose.")
            break
    elif action == 'stand':
        break

# Dealer's turn
while dealer_hand.value < 17:
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.calculate_value()

print("Dealer's hand:", dealer_hand)
if dealer_hand.value > 21:
    print("Dealer busts! You win.")
elif dealer_hand.value >= player_hand.value:
    print("Dealer wins.")
else:
    print("Player wins.")