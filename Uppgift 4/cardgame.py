import os
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return f"{self.suit} {self.value}"
    
    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
        return f"{self.suit} {self.value}"




def creat_deck():
    cards = []

    suits =  ["♠", "♥", "♣", "♦"]
    values = ["ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    for suits in suits:
        for value in values:
            cards.append(cards(value, suits))

    return cards
os.system("cls" if os.name=="nt" else "clear")

cards = creat_deck()
print (cards)

#skapa ett kort

#["♠", "♥", "♣", "♦"]
os.system("cls")


cards = []
cards.append(Card("♠", 2))
cards.append(Card("♠", 3))
cards.append(Card("♠", 4))
cards.append(Card("♠", 5))


print(cards)