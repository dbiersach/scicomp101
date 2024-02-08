# logistics_map.py

import numpy as np
from simple_screen import SimpleScreen
from pygame import Color


def plot_logistics_map(ss):
    blue = Color("blue")

    # For every screen pixel in a row
    for sx in range(ss.screen_width):
        # Get world x coordinate of the current screen x coordinate
        x = ss.world_x(sx)
        # Pick a random starting world y coordinate
        y = np.random.random()

        # Iterate (but don't draw) to reach a stable orbit
        for _ in range(5000):
            y = x * y * (1 - y)

        # Now draw each pixel in the stable orbit
        for _ in range(500):
            y = x * y * (1 - y)
            # Color pixel based upon current world (x, y) coordinate
            ss.set_world_pixel(x, y, blue)


def main():
    ss = SimpleScreen(
        world_rect=((2.5, 0.0), (4.0, 1.0)),
        draw_function=plot_logistics_map,
        screen_size=(900, 900),
        title="Logistics Map",
    )
    ss.show()


main()
