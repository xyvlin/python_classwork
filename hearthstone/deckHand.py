import random

class Deck():
    def __init__(self, cards):
        self.cards=cards
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else: # no cards to draw from
            return None

class Hand():
    def __init__(self):
        self.cards=[]
    # add a card to hand
    def add_c(self, card):
        if len(self.cards)<10:
            self.cards.append(card)
    # take out a card from hand 
    def play_c(self, card_i):
        return self.cards.pop(card_i)
