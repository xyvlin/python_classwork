from effects import *
from hearthstone import ask_target

# display cards in a list 
def display_cards(cards):
    count=1
    for c in cards:
        print(f"\t{count}. {c}")
        count+=1

# ask for input; min and max are inclusive
def choose_card(prompt, min, max):
    while True:
        try:
            x = int(input(prompt))
            assert(min <= x <= max)
            break
        except Exception:
            print("please enter a valid card number or 0")
    return x

# result shows players' health and who wins; player healths don't go below 0
def result(player1,player2):
    print("==============RESULT===============")
    print(f"{player1.name}'s health: {max(player1.health,0)}")
    print(f"{player2.name}'s health: {max(player2.health,0)}")
    if player1.health<=0 and player2.health<=0:
        print("it's a tie :O")
    elif player1.health<=0:
        print(f"{player2.name} won")
    else:
        print(f"{player1.name} won")

# change the parameters for spell's effect
def get_effect_parameters(effect, cur, oppo):
    if effect == fireball_effect:
        return [ask_target(oppo)]
    elif effect == polymorph_effect:
        return [ask_target(oppo)]
    elif effect == flame_effect:
        return [oppo]
    elif effect == draw2_effect:
        return [cur]
    elif effect == holy_nova:
        return [cur,oppo]
    elif effect == catalysm:
        return [cur,oppo]
    elif effect == shot:
        return [oppo]
    elif effect == boost1_effect:
        return [cur]