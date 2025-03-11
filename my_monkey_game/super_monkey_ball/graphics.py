import pygame
import pymunk

def draw(screen, game_state):
    screen.fill((255, 255, 255))
    for shape in game_state.space.shapes: #access the shapes from the space object
        if isinstance(shape, pymunk.Segment):
            p1 = shape.a
            p2 = shape.b
            pygame.draw.line(screen, (0, 255, 0), p1, p2,5)
        if isinstance(shape, pymunk.Circle):
            p = shape.body.position
            pygame.draw.circle(screen, (255, 0, 0), p, shape.radius)