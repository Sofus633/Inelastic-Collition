import random
import math
from simulation import Simulation
from ball import Ball
from settings import FPS
from settings import screen, SCREEN_SIZE
from vector2 import Vector2


def createposition(simulation):
    center = SCREEN_SIZE[0] /2 - 200, SCREEN_SIZE[1] /2 - 150
    angle1 = 0

    for i in range(20):
        angle1 += 10
    
        simulation.addball(Ball(Vector2(center[0] + (math.sin(angle1) + 1 )* 100, center[1] + (math.cos(angle1) + 1 )* 100),Vector2(math.sin(angle1), math.cos(angle1))))

    
def mainloop():
    simu = Simulation(screen, autostart=False)
    simu.addball(Ball(Vector2(10,20),Vector2(1, 0)))
    createposition(simu)
    simu.start()
    
    
mainloop()