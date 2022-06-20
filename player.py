import numpy as np


class Player:
    
    def __init__(self, name, initial_budget=1500):
        self.name = name
        self.budget = initial_budget
        self.position = 0
        self.properties = []
        
        
    def throw_dices(self):
        outcome = np.random.randint(low=1, high=7) + np.random.randint(low=1, high=7)
        self.position += outcome
        
    def buy_property(self):
        pass
    
    def rent_payment(self):
        pass
    
    def tax_payment(self):
        pass
    
    def go_to_prison(self):
        pass
    
    def card_draw_probability(self):
        pass
    
    def card_draw_unexpected(self):
        pass
    
    def build_house(self):
        pass
    
    def build_hotel(self):
        pass

