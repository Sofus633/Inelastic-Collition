from settings import screen
import pygame

def display_b(ball):
    pygame.draw.circle(screen , (255, 0, 2), ball.pos.get(), ball.size)