import numpy as np

class player:
    def __init__(self, x_orientation, y_orientation, width, height):
        self.x_orientation = x_orientation
        self.y_orientation = y_orientation
        self.width = width
        self.height = height

        self.score = 0

class ball:

    def __init__(self, radius, x_orientation, y_orientation):
        self.radius = radius
        self.x_orientation = x_orientation
        self.y_orientation = y_orientation
        self.speed = 8
        self.direction = np.random.uniform(-1, 1, (2)).round(2)