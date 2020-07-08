
class Territory( object ):
    """Model a territory in axis and allies"""
    
    def __init__(self, nation, adj_territories, units, name):
        """
        Initialize the territory with a nation, and adjacent territories
        """
        #Start with blank values        
        self.__nation = "neutral"
        self.__adj_territories = []
        self.__units = []
        self.__name = ""
        
        #If the parameters are of the correct type update the corresponding values
        if type(nation) == str:
            self.__nation = nation
        if type(name) == str:
            self.__name = name
        if type(adj_territories) == list:
            self.__adj_territories = adj_territories
        if type(units) == list:
            self.__units = units
    
    def __str__( self ):
        """Return a string representation of the territory"""
        return self.__name
    
    def __repr__( self ):
        return self.__name  
          
    def nation( self ):
        """Return the territory's controlling nation"""
        return self.__nation
    
    def adj_territories( self ):
        return self.__adj_territories
        
    def units( self ):
        """Return territory's units"""
        return self.__units
    
    def capture_territory(self, nation):
        """Changes the territory's nation for when a new power captures it"""
        self.__nation == nation
        
    def destroy_units(self, units):
            """
            Removes units from a territory given a list of units to remove
            """
            for destroy_unit in units:
                self.__units.remove(destroy_unit)

    
    

class Land( Territory ):
    """"Land Territory"""
    def __init__(self, nation, adj_territories, units, name, IC, capital,
                 units_produced, value):
        super().__init__(self, nation, adj_territories, units, name)
        #IC determines if there is an industrial complex in the territory and
        #whether the IC was built(2) or existed at the start of the game(1)
        #with (0) representing no IC
        self.__IC = 0
        self.__capital = False
        self.__units_produced = 0
        #Value is the IPC value of the territory
        self.__value = 0
        if type(IC) == int:
            if IC <= 2 and IC >= 0:
                self.__IC = IC
        if type(capital) == bool:
            self.__capital = capital
        if type(value) == int:
            self.__value = value
            
        def industrial_complex( self ):
            """Returns whether there is an IC on the terriory and if so what type""" 
            return self.__IC
        
        def capital( self ):
            """Returns whether the nation is a captial"""
            return self.__capital
        
        def units_produced( self ):
            """Returns how many units the territory has produced this turn"""
            return self.__units_produced
        
        def value( self ):
            """Returns the IPC value of the territory"""
            return self.__value
        
        def create_units(self, units):
            """
            Creates units on a territory while tracking whether the territory
            has an IC to produce with, and if so how many units it has produced
            """
            if self.__IC > 0:
                for unit in units:
                    if self.__IC == 1:
                        if self.__units_produced < value:
                            self.__units.append(unit)
                            self.__units_produced += 1
                    elif self.__IC == 2:
                        self.__units.append(unit)
                        
                        
        def increase_units_produced(self):
            """Allows other things to modify the units produced value"""
            self.__units_produced += 1
                    
                
        def cleanup(self):
            """
            Resets the units_produced value for starting the next turn
            """
            self.__units_produced = 0
                        
        
        
class Sea( Territory ):
    """Sea Territory"""
    def __init__(self, nation, adj_territories, units, name):
        super().__init__(self, nation, adj_territories, units, name)
        
    def create_units(self, units, territory):
        for unit in units:
            if territory.industrial_complex() == 1:
                if territory.units_produced() < territory.value():
                    self.__units.append(unit)
                    territory.increase_units_produced()
            elif territory.inductrial_complex() == 2:
                self.__units.append(unit)
                    
                
        
        
        
        
        
        
        
        
        