# ifs.py

import numpy as np
from pygame import Color
from dataclasses import dataclass


@dataclass
class Transform:
    def __init__(self):
        self.x1 = 0.0
        self.y1 = 0.0
        self.x2 = 0.0
        self.y2 = 0.0
        self.x3 = 0.0
        self.y3 = 0.0
        self.color = Color("black")
        self.probability = 0.0
        self.m = np.zeros((3, 3))


@dataclass
class IteratedFunctionSystem:
    def __init__(self):
        self.transforms = []
        self.affine_width = 0.0
        self.affine_height = 0.0
        self.cdf = 0.0

    def set_base_frame(self, x_min, y_min, x_max, y_max):
        self.affine_width = x_max - x_min
        self.affine_height = y_max - y_min
        return

    # fmt: off
    def add_mapping(self, x_left, y_left, x_right, y_right,
                     x_top, y_top, color, probability):
    #fmt: on
        # Probabilities accumulate across mappings
        self.cdf += probability

        t = Transform()
        t.x1 = x_left
        t.y1 = y_left
        t.x2 = x_right
        t.y2 = y_right
        t.x3 = x_top
        t.y3 = y_top
        t.color = color
        t.probability = self.cdf
        self.transforms.append(t)

    def generate_transforms(self):
        for t in self.transforms:
            coeffs = np.array([
                [0, 0, 1],
                [self.affine_width, 0, 1],
                [0, self.affine_height, 1]
            ])

            # Solve systems of 3x3 equations to get transformation matrix
            vals = np.array([t.x1, t.x2, t.x3])
            sol = np.linalg.solve(coeffs, vals)
            t.m[0, 0] = sol[0]
            t.m[1, 0] = sol[1]
            t.m[2, 0] = sol[2]

            vals = np.array([t.y1, t.y2, t.y3])
            sol = np.linalg.solve(coeffs, vals)
            t.m[0, 1] = sol[0]
            t.m[1, 1] = sol[1]
            t.m[2, 1] = sol[2]

            # Last column in transformation matrix is always this
            t.m[0, 2] = 0
            t.m[1, 2] = 0
            t.m[2, 2] = 1

    def transform_point(self, x, y):
        p = np.random.random()
        for t in self.transforms:
            if p <= t.probability:
                xt: float = x * t.m[0, 0] + y * t.m[1, 0] + t.m[2, 0]
                yt: float = x * t.m[0, 1] + y * t.m[1, 1] + t.m[2, 1]
                return xt, yt, t.color        
        # This should never happen if the mapping
        # probabilities all sum to 1.0
        return 0, 0, Color("black")
