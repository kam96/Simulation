import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
from test.datetimetester import Oddballs
from concurrent.futures._base import RUNNING

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
simultons = set()
steps = False
obj = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, steps, obj
    running = False
    cycle_count = 0
    simultons = set()
    steps = False
    obj = None
    
#start running the simulation
def start ():
    global running 
    running = True

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False

#step just one update in the simulation
def step ():
    global steps, running
    steps = True
    running = True

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global obj
    obj = kind

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y): 
    if str(obj) == "Remove":
        for sim in find(lambda s: s.contains((x,y))):
            remove(sim)
    elif obj != None:
        objStr = str(obj) + '({},{})'.format(x,y)
        simultons.add(eval(objStr))

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    
# remove simulton s from the simulation    
def remove(s): 
    global simultons
    simultons.discard(s)
    
#find/return a set of simultons that each satisfy predicate p    
def find(p): 
    simSet = set()
    for sims in simultons:
        if p(sims): simSet.add(sims)
    return simSet

#call update for every simulton in the simulation
def update_all(): 
    global running, cycle_count, steps
    if running:
        cycle_count += 1
        for s in set(simultons):
            s.update(model)
        if steps:
            running = False
            steps = False

#delete from the canvas every simulton in the simulation; then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all(): 
    for sim in controller.the_canvas.find_all():
        controller.the_canvas.delete(sim)
    for sim in simultons:
        sim.display(controller.the_canvas)
    controller.the_progress.config(text=str(len(simultons))+
        " simultons/" +str(cycle_count)+" cycles")