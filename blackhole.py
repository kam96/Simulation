# A Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2, Black_Hole.radius*2)
    
    def update(self, model):
        def finder(sim):
            if isinstance(sim, Prey) and self.contains(sim.get_location()):
                return True
        simset = model.find(finder)
        for sim in simset:
            model.remove(sim)
        return simset
        
    def display(self, canvas):
        canvas.create_oval(self._x-self._width,self._y-self._height,
                           self._x+self._width,self._y+self._height,
                           fill='black')
    
    def contains(self, xy):
        if self.distance(xy) < self._width: return True
        else: return False