import datetime
import time
import pygame
from display import display_b
from settings import getid, setjsonvalue, FPS
class Simulation:
    def __init__(self, screen, balls = [],id=getid(), autostart = True):
        self.id = id
        self.balls = [*balls]
        self.screen = screen
        self.champ = []
        self.current_time = time.perf_counter()
        self.dt = 0
        self.createlog()
        self.running = True
        if autostart:
            self.compframe_loop()
        print("e")
        
    def start(self):
        self.compframe_loop()
        
    def createlog(self):
        setjsonvalue(self.id,  {"balls" :[ball.get for ball in self.balls], "champ" : [champ.get for champ in self.champ]} )

        print(f"{self.id} simulation added to log at current state {datetime.datetime.now()}")
        
        
    def compframe_update_d(self):
        for ball in self.balls:
            display_b(ball)
            ball.update()
        
    def ref_disp(self):
        pygame.display.flip()
        self.screen.fill((200, 200, 200))
        

        
    def compframe_loop(self):
        prev_time = time.perf_counter()
        current_time = prev_time

        while self.running:

            prev_time = current_time
            self.current_time = time.perf_counter()
            self.dt = self.current_time - prev_time 

            self.compframe_update_d()
            self.ref_disp()
            time.sleep(max(0, (current_time + 1.0/FPS) - time.perf_counter()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
    def addball(self, ball):
        self.balls.append(ball)
        
    