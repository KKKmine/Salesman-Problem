import numpy as np
from Individual import Individual

class Map:
    def __init__(self, pointSize, posRange):
        Individual.map = self
        Individual.pointSize = pointSize
        self.pointX = np.random.random_sample(size = pointSize) * posRange
        self.pointY = np.random.random_sample(size = pointSize) * posRange