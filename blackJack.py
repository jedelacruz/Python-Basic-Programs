import random

print("===================== BLACKJACK =====================")
print()

class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.cards = [self.deck.get_card(), self.deck.get_card()]

    def get_value(self):
        value = 0
        for card in self.cards:
            value += card
        return value

    def hit(self):
        self.cards.append(self.deck.get_card())

class Player:
    def __init__(self, deck):
        self.hand = Hand(deck)

    def play(self):
        while self.hand.get_value() < 21:
            print("Current hand is worth %d" % self.hand.get_value())
            action = input("Do you want to hit or stand? ")
            if action == "hit":
                self.hand.hit()
            else:
                break

class Dealer:
    def __init__(self, deck):
        self.hand = Hand(deck)

    def play(self):
        while self.hand.get_value() < 17:
            self.hand.hit()

deck = Deck()
player = Player(deck)
dealer = Dealer(deck)

player.play()
print("Player busts" if player.hand.get_value() > 21 else "Player stands with value %d" % player.hand.get_value())

dealer.play()
print("Dealer busts" if dealer.hand.get_value() > 21 else "Dealer stands with value %d" % dealer.hand.get_value())

if dealer.hand.get_value() > 21 or player.hand.get_value() <= 21 and player.hand.get_value() > dealer.hand.get_value():
    print("Player wins!")
else:
    print("Dealer wins!")
