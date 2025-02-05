from vector2 import Vector2
from settings import SCREEN_SIZE
class Ball:
    def __init__(self,pos = Vector2(), velo = Vector2()):
        self.pos = pos
        self.velo = velo
        self.angvelo = 0 #angle
        self.size = 10
        
    def get(self):
        return {
            "position" : self.pos.get_js(),
            "velocity" : self.velo.get_js(),
            "anglvelo" : self.angvelo,
            "size" : self.size
        }
        
    def update(self):
        newpos = self.pos + self.velo
        if newpos.x > SCREEN_SIZE[0] - self.size or newpos.x < self.size:
            self.velo.x = -self.velo.x * .8
        if newpos.y > SCREEN_SIZE[1] - self.size or newpos.y < self.size:
            self.velo.y = -self.velo.y * .8
        self.pos = self.pos + self.velo
        