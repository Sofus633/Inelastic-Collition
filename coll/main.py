import random
from simulation import Simulation
from ball import Ball
from settings import FPS
from settings import screen
from vector2 import Vector2




def mainloop():
    simu = Simulation(screen, autostart=False)
    for i in range(5):
        simu.addball(Ball(Vector2(randoms=True, ranges=(0, 100)), Vector2(randoms=True, ranges=(0, 1))))
    simu.start()
    
    
mainloop()