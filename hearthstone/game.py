# import stuff from the other files 
from cardClasses import Minion
from cardClasses import Spell
import helpers
"""
This module contains all the basic game functions. 
The functions are called in main.py
"""
# play cards from hand (use spell or place minion) 
def play_cards(cur,oppo,round):
    cur.set_crystal(round) #set crystal to round or 10 if round exceed 10
    choice=10
    while(choice==10): 
        print("Your mana crystal:",cur.crystal) # show crystal number
        # ask for a move (number for card; 0 for quit)
        choice = helpers.choose_card("Which card do you want to play (Index of your card; 0 to end): ",0,len(cur.hand.cards))
        # chose to quit
        if choice==0:
            print("now you can command your minions to attack")
            break
        # input is a card but the field is full
        elif cur.field.full():
            print("your field cannot hold over 7 minions")
        # input is a card and has enough crystal to play the card
        elif cur.hand.cards[choice-1].cost<=cur.crystal:
            choice-=1 # translate into array index
            cur.crystal-=cur.hand.cards[choice].cost # adjust crystal number
            # if it's a minion, put it on battlefield
            if isinstance(cur.hand.cards[choice],Minion): 
                cur.play_card(choice)
            # if it's a spell, ask for target and attack
            elif isinstance(cur.hand.cards[choice],Spell):
                # pass parameters needed for this spell's effect
                para = helpers.get_effect_parameters(cur.hand.cards[choice].effect,cur,oppo)
                temp = cur.hand.cards[choice].play(para)
                print(temp)
                if temp == "spell casted":
                    cur.hand.cards.pop(choice) # erase card from hand
                else: 
                    # card isn't played so add back cost
                    cur.crystal+=cur.hand.cards[choice].cost 
            display(cur,oppo)
        # too poor 
        else:
            print("you don't have enough crystal to play this card")  
        choice=10 # reset choice to ask again

# ask for target when player wants to attack; return object
def ask_target(oppo):
    # ask for index of card or 0 for directly attacking the opponent 
    tar = helpers.choose_card("who do you want to attack? (enter card index or 0 for opponent): ",0,len(oppo.field.minions))
    if tar==0: # directly attacking opponent 
        return oppo
    else: # return the chosen minion
        return oppo.field.minions[tar-1]

# run attack procedure
def attack(cur,oppo):
    cur.field.reset_attack_count() # reset the number of attacks launched to 0
    display(cur,oppo) #display the field 
    choice=10
    while choice==10:
        # input for attacking minion 
        choice = helpers.choose_card("which minion should launch the attack? (enter card index or 0 to end turn): ",0,len(cur.field.minions))
        if choice == 0: # end turn 
            print(f"{cur.name}'s turn ended.")
            break
        elif not cur.field.minions[choice-1].awake: # 1st round: minion cannot attack
            print("this minion is currently sleeping")
            choice=10   
        elif cur.field.minions[choice-1].alr_attack(): # minion has already attacked this round so can't attack
            print("each minion can only attack once")
            choice=10
        else: # start attack procedure 
            choice-=1 # adjust choice to actual index
            tar=ask_target(oppo) # return reference to the chosen target
            if tar==None: # just in case
                choice=10
            # player choose another minion when taunt minion is on the field
            elif helpers.tauntExist(oppo.field.minions) and tar.description != "Taunt":
                print("you must attack the taunting minion")
                choice=10
            elif tar==oppo: # attack player 
                oppo.attacked(cur.field.minions[choice].attack)
                cur.field.minions[choice].attack_count+=1# the target has stealth effect so player cannot attack it
            elif tar.description == "Stealth":
                print("your minion cannot attack a minion with stealth effect")
                choice=10
            else: # attack minion
                cur.field.minions[choice].play(tar)
            choice=10 # reset choice to ask again
    helpers.clean_field(cur,oppo) # clean up all corpse on field

# display field & current player's hands; players are index 0; cards start from 1
def display(cur,oppo): 
    helpers.clean_field(cur,oppo) # clean up all corpse on field
    print("OPPONENT BATTLEFIELD:")
    print(f"\t0. {oppo.name} - health: {oppo.health}")
    helpers.display_cards(oppo.field.minions)
    print("YOUR BATTLEFIELD:")
    print(f"\t0. {cur.name} - health: {cur.health}")
    helpers.display_cards(cur.field.minions)
    print("YOUR HAND:")
    helpers.display_cards(cur.hand.cards)
    print()

def init_game(player1,player2):
    # set up player's names, shuffle their cards, and draw starting hands
    print("=========PLAYERS SETTING==========")
    player1.name=input("\tfirst player's name: ")
    player1.deck.shuffle()
    player1.starting_hand(3)
    player2.name=input("\tsecond player's name: ")
    player2.deck.shuffle()
    player2.starting_hand(4)
    print("============GAME START============")

# runs one round of game for current player
def gamePlay(cur,oppo,round):
    print(f"{cur.name}'s TURN")
    cur.take_turn() # draw card, reset crystal, wake minions up
    if cur.health<=0 or oppo.health<=0: # if players die from drawing cards stop the game
        return
    print("---------PLAY CARD--------")
    display(cur, oppo)
    play_cards(cur, oppo, round)
    print("\n----------ATTACK----------")
    attack(cur, oppo)