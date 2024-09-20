from cardClasses import Minion
import random

# spell effects (parameters are lists, hence the [0])
def fireball_effect(target):
    target[0].health -= 6  
    return "spell casted"

def polymorph_effect(target):
    if isinstance(target[0],Minion):
        target[0].attack = 1
        target[0].health = 1
        target[0].name = "Sheep"
        return "spell casted"
    else:
        return "you cannot turn opponent player into a sheep"

def flame_effect(oppo):
    for m in oppo[0].field.minions:
        m.health-=5
    return "spell casted"

def draw2_effect(cur):
    cur[0].starting_hand(2)
    return "spell casted"

def holy_nova(para): # 0=cur 1=oppo
    for m in para[1].field.minions:
        m.health-=2
    for m in para[0].field.minions:
        m.health+=2
    return "spell casted"

def catalysm(para): # 0=cur 1=oppo
    if len(para[0].hand.cards)<2:
        return "no card to discard"
    for i in range(len(para[0].field.minions)):
        para[0].field.minions.pop(0)
    for i in range(len(para[1].field.minions)):
        para[1].field.minions.pop(0)
    para[0].hand.cards.pop(random.randint(0,len(para[0].hand.cards)-1))
    para[0].hand.cards.pop(random.randint(0,len(para[0].hand.cards)-1))
    return "spell casted"

def shot(oppo):
    if oppo[0].field.minions:
        oppo[0].field.minions.pop(random.randint(0,len(oppo[0].field.minions)-1))
        return "spell casted"
    return "no minion to shoot"

def boost1_effect(cur):
    for m in cur.field.minions:
        if m.effect is not boost1_effect:
            m.health+=1
            m.attack+=1

def cancel_boost1(curField):
    for m in curField.minions:
        m.health-=1
        m.attack-=1
