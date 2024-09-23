"""
These are classes for the cards. 
"""
class Card():
    def __init__(self, name, cost, description):
        self.name=name
        self.cost=cost
        self.description=description    
    def play(self):
        pass
    def __str__(self):
        return f"{self.name} (mana cost: {self.cost}) - {self.description}"

class Minion(Card):
    def __init__(self, name, cost, attack, health, description, effect=None, cancel_effect=None):
        super().__init__(name, cost, description)
        self.health=health
        self.attack=attack
        self.awake = False
        if description is "Charge":
            self.awake = True
        self.effect=effect
        self.cancel_effect=cancel_effect
        self.attack_per_round=1 # each minion attack up to once per round unless has special effect
        self.attack_count=0 # number of attack launched in a round
    def play(self, target): # attack target minion
        target.health-=self.attack # self attack enemy
        self.health-=target.attack # enemy attack self
        self.attack_count+=1 
    def alr_attack(self): # True if the minion cannot attack anymore
        return self.attack_count>=self.attack_per_round
    def __str__(self): # add attack & health to display
        return f"{self.name} - cost: {self.cost}; attack: {self.attack}; health: {self.health}; {self.description}"

class Spell(Card):
    def __init__(self, name, cost, description, effect):
        super().__init__(name,cost,description)
        self.effect=effect
    def play(self, para): # attack target
        return self.effect(para)