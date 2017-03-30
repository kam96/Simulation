# A Hunter is derived from a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    constant = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self, x, y, Pulsator.radius*2, Pulsator.radius*2, 0, 5)
        self.randomize_angle()
    
    def update(self,model):
        self.move()
        Pulsator.update(self, model)
        sims = model.find(lambda s: isinstance(s, Prey))
        for sim in sims:
            if self.distance(sim.get_location()) <= self.constant:
                self.set_angle(atan2(sim.get_location()[1]-self.get_location()[1], 
                                     sim.get_location()[0]-self.get_location()[0]))
        
