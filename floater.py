# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage
from prey import Prey
from random import random, randrange, uniform

class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,Floater.radius*2,Floater.radius*2,0,5)
        self.randomize_angle()
    
    def update(self,model):
        if random() < .3:
            speed = uniform(-.5,.5)
            if 3 < self._speed + speed < 7:
                self._speed = self._speed + speed
            angle = uniform(-.5,.5)
            self._angle = self._angle + angle
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius,self._y-Floater.radius,
                           self._x+Floater.radius,self._y+Floater.radius,
                           fill='red')