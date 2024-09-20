class Field():
    def __init__(self, minions):
        self.minions=minions

    # place minions in field 
    def add_m(self, minion):
        self.minions.append(minion)

    # wake up all minions on field
    def wake_m(self):
        for m in self.minions:
            m.awake = True

    # check whether the field is full
    def full(self):
        return len(self.minions)>=7
    
    # clean up corpse & cancel the effect of dead minions
    def clean(self):
        cancel = []
        for m in self.minions:
            if m.effect and m.health<=0:
                cancel.append(m)
        for c in cancel:
            c.cancel_effect(self)
        for m in self.minions:
            if m.health<=0:
                self.minions.remove(m)

    # reset number of attacks launched to 0
    def reset_attack_count(self):
        for m in self.minions:
            m.attack_count=0 