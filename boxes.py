#import numpy as np
        

###############################################################################       
class land_box:
    
    def __init__(self, name, land_price, house_price, 
                 hotel_price, mortage_price,
                 land_income, one_house_income,
                 two_house_income, three_house_income,
                 four_house_income, hotel_income):
        
        self.name = name
        self.land_price = land_price
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.mortage = mortage_price
        self.land_income = land_income
        self.one_house_income = one_house_income
        self.two_house_income = two_house_income
        self.three_house_income = three_house_income
        self.four_house_income = four_house_income
        self.hotel_income = hotel_income
        
        self.owner = None
        self.num_houses = 0
        self.hotel = False

 
###############################################################################       
class station_box:
    
    def __init__(self, name, station_price,
                 single_income, double_income,
                 triple_income, quadruple_income,
                 mortage_price):
        
        self.name = name
        self.station_price = station_price
        self.single_income = single_income
        self.double_income = double_income
        self.triple_income = triple_income
        self.quadruple_income = quadruple_income
        self.mortage = mortage_price
        
        self.owner = None
        
###############################################################################       
class company_box:
    
    def __init__(self, name, company_price, mortage_price,
                 single_company_income, double_company_income):
            
            self.name = name
            self.company_price = company_price
            self.mortage = mortage_price
            self.single_company_income = single_company_income
            self.double_company_income = double_company_income
            
            self.owner = None
            
###############################################################################           
class tax_box:
    
    def __init__(self, name, tax_value):
        self.tax_value = tax_value
        
        
###############################################################################        
class probability_box:
    
    def __init__(self):
        self.name = 'Probability'
 
    
###############################################################################       
class unexpected_box:
    
    def __init__(self):
        self.name = 'Unexpected'
        

###############################################################################
class parking_box:
    
    def __init__(self):
        self.name = 'Parking'
        
        
###############################################################################
class prison_box:
    
    def __init__(self):
        self.name = 'Prison'


###############################################################################
class start_box:

    def __init__(self):
        self.name = 'Start'


###############################################################################
class go_to_prison_box:
    
    def __init__(self):
        self.name = 'Go to Prison'
        
        