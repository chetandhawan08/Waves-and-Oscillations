import numpy as np


class SpringForce:
    def __init__(self, k):
        self.k = k

    def compute(self, particle):
        return -self.k * particle.position


class DampingForce:
    def __init__(self, gamma):
        self.gamma = gamma

    def compute(self, particle):
        return -self.gamma * particle.velocity
