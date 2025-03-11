import pymunk

class Ball:
    def __init__(self, space, x, y, radius):
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius))
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.8
        space.add(self.body, self.shape)

    def get_position(self):
        return self.body.position