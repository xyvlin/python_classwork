class Player():
    def __init__(self, name, deck, hand, field, crystal):
        self.name=name
        self.deck=deck
        self.hand=hand
        self.field=field
        self.crystal=crystal
        self.health=30
        self.attack=0 # for Minion.play() to work
        self.penalty=0 # the amount of health taken for drawing from empty deck
    # draw starting hand according to num
    def starting_hand(self, num):
        for i in range(num):
            c = self.deck.draw_card()
            if c:
                self.hand.add_c(c)
            else:
                print("no card to draw from")
    # wake up all minions and draw one card; if no card in deck health--
    def take_turn(self):
        self.field.wake_m()
        c = self.deck.draw_card()
        if c == None: # no card in deck 
            self.penalty+=1
            print(f"you don't have any card to draw from so health {self.health} - {self.penalty}")
            self.health-=self.penalty
        else:
            self.hand.add_c(c)
    # reduce player's health when attacked 
    def attacked(self,dam):
        self.health-=dam
    # place minion in battlefield
    def play_card(self, car_ind):
        c = self.hand.play_c(car_ind)
        self.field.add_m(c)
        if c.effect:
            c.effect(self)
    #set player's crystal for the round
    def set_crystal(self, round):
        if round<10:
            self.crystal = round
        else:
            self.crystal = 10
