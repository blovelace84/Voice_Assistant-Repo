import pymunk
from my_monkey_game.super_monkey_ball import physics
from my_monkey_game.super_monkey_ball import level


class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.space = pymunk.Space()
        self.space.gravity = (0, 980)
        level_data = level.load_level("super_monkey_ball/assets/levels/level1.txt")
        self.level = level.Level(self.space, level_data)
        self.ball = physics.Ball(self.space, 400, 100, 20)

    def update(self):
        self.space.step(1/60.0)