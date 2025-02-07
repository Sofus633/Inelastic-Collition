import datetime
import time
import pygame
import numpy as np
from vector2 import Vector2
import math
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

    def is_collide(self, ball1, ball2):
        distance = math.sqrt(
                (ball1.pos.x - ball2.pos.x)**2 +
                (ball1.pos.y - ball2.pos.y)**2
        )
        if distance < ball1.size +  ball2.size:
            return True
        return False
        
        
    def checkcollition(self):
        for i in range(len(self.balls)):
            for y in range(i+1, len(self.balls)):
                distance = math.sqrt(
                    (self.balls[i].pos.x - self.balls[y].pos.x)**2 +
                    (self.balls[i].pos.y - self.balls[y].pos.y)**2
                )
                if distance < self.balls[i].size +  self.balls[y].size:
                    self.is_collide(self.balls[i], self.balls[y])

    def as_collide(self, ball1, ball2):

        m1, m2 = ball1.mass, ball2.mass
        v1, v2 = np.array([ball1.velo.x, ball1.velo.y]), np.array([ball2.velo.x, ball2.velo.y])
        p1, p2 = np.array([ball1.pos.x, ball1.pos.y]), np.array([ball2.pos.x, ball2.pos.y])
        r1, r2 = ball1.size , ball2.size   # Radii of the balls

        # Relative position and velocity
        rel_pos = p1 - p2
        rel_vel = v1 - v2
        dx, dy = ball1.pos.x- ball2.pos.x, ball1.pos.y - ball2.pos.y
        distance = math.sqrt(dx**2 + dy**2)
        min_distance = r1 + r2


        if distance == 0:
            distance = 0.01  # Avoid division by zero

        # Normalize relative position
        rel_pos_unit = rel_pos / distance

        # Calculate new velocities after collision
        dot_product = np.dot(rel_vel, rel_pos_unit)
        v1_final = v1 - (2 * m2 / (m1 + m2)) * dot_product * rel_pos_unit
        v2_final = v2 + (2 * m1 / (m1 + m2)) * dot_product * rel_pos_unit

        # Update positions to avoid overlap
        overlap = min_distance - distance 
        if distance == 0:  
            distance = 0.01
        dx /= distance 
        dy /= distance
        ball1.pos += Vector2(dx * overlap / 2, dy * overlap / 2)  
        ball2.pos -= Vector2(dx * overlap / 2, dy * overlap / 2) 
        
        # Apply friction to final velocities
        friction = 0.99
        v1_final *= friction
        v2_final *= friction

        # Update ball attributes

        print()
        tolst1 = v1_final.tolist()
        tolst2 = v2_final.tolist()
        ball1.velo = Vector2(tolst1[0], tolst1[1])
        ball2.velo = Vector2(tolst2[0], tolst2[1])
        
    def as_collide2(self, ball1, ball2):
        reC = 1
        newspeed1 =  ((ball2.velo - ball1.velo) * reC+  ball1.velo * ball1.mass + ball2.mass * ball2.velo ) / (ball1.mass + ball2.mass)
        newspeed2 =  ((ball1.velo - ball2.velo) * reC +  ball2.velo * ball2.mass + ball1.mass * ball1.velo ) / (ball2.mass + ball1.mass)
        ball1.velo = newspeed1
        ball2.velo = newspeed2
    def check_collitions(self):
        for i in range(len(self.balls)-1):
            for y in range(i + 1, len(self.balls)):
                if self.is_collide(self.balls[i], self.balls[y]):
                    self.as_collide2(self.balls[i], self.balls[y])   
                    
    def compframe_loop(self):
        prev_time = time.perf_counter()
        current_time = prev_time

        while self.running:
            prev_time = current_time
            self.current_time = time.perf_counter()
            self.dt = self.current_time - prev_time 
            self.check_collitions()
            self.compframe_update_d()
            self.ref_disp()
            time.sleep(max(0, (current_time + 1.0/FPS) - time.perf_counter()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
    def addball(self, ball):
        self.balls.append(ball)
        
    