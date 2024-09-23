from playerClasses import Player
import helpers
from game import init_game
from game import gamePlay
from deckHand import Deck
from deckHand import Hand 
from field import Field
from cards import set_up_deck
"""
This module runs the actual game:
    1. initialize players
    2. display cards 
    3. set up player names 
    4. game loop 
    5. display game result
"""
# initialize decks and players and turns
deck1=set_up_deck()
deck2=set_up_deck()
player1 = Player("",Deck(deck1),Hand(),Field(list()),1)
player2 = Player("",Deck(deck2),Hand(),Field(list()),1)

# show all cards in a deck
print("===============CARDS===============")
helpers.display_cards(deck1)

init_game(player1,player2) # display cards & set up players
turn=1 # for keeping track of current round number (2 turns per round)
while (player1.health>0 and player2.health>0):
    if turn%2==1:# odd = player1's turn
        print(f"==========ROUND {(turn+1)//2}==========")
        gamePlay(player1,player2,(turn+1)//2)
    else: # player2's turn
        gamePlay(player2,player1,(turn+1)//2)
    turn+=1 
    print("========================================")
helpers.result(player1,player2) # when the game is done, display result