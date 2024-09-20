from cardClasses import Minion
from cardClasses import Spell
from effects import *
import copy

# all cards
minions = [
    Minion("Chillwind Yeti", 4, 4, 5, "A classic yeti minion with solid stats."),
    Minion("Boulderfist Ogre", 6, 6, 7, "A powerful ogre minion with high attack and health."),
    Minion("Bloodfen Raptor", 2, 3, 2, "A simple raptor minion with good stats for its cost."),
    Minion("Stormwind Champion", 7, 6, 6,"Your other minions have +1/+1",boost1_effect,cancel_boost1)
]
spells = [
    Spell("Fireball", 4, "Deal 6 damage.", fireball_effect),
    Spell("Polymorph", 4, "Transform a minion into a 1/1 Sheep.", polymorph_effect),
    Spell("Flamestrike",7,"Deal 5 damage to all enemy minions",flame_effect),
    Spell("Arcane Intellect",3,"Draw 2 cards", draw2_effect),
    Spell("Holy Nova",3,"Deal 2 damage to all enemies, and restore 2 Health to all friendly characters",holy_nova),
    Spell("Catalystm",5,"Destroy all minions and discard 2 cards", catalysm),
    Spell("Deadly Shot",3, "destroy a random enemy minion",shot)
]
# put minions and spells cards into the deck
def set_up_deck():
    deck=copy.deepcopy(minions)
    deck.extend(copy.deepcopy(spells))
    return deck
