#Class special is an erratic type of Prey which
# constantly randomizes its speed and angle

from random import uniform,randint
from math import pi
from prey import Prey

class Special(Prey):
    radius = 2.5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,Special.radius*2,Special.radius*2,0,8)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        self.set_velocity(randint(1,9), uniform(0,pi*2))
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius,self._y-Special.radius,
                           self._x+Special.radius,self._y+Special.radius,
                           fill='green')