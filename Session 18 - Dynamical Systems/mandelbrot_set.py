# mandelbrot_set.py

from pygame import Color
from simple_screen import SimpleScreen


def plot_mandelbrot_set(ss):
    radius, max_iter = 16, 100
    clr = Color(0)  # Black
    # For each screen pixel row
    for sy in reversed(range(ss.screen_height)):    
        # For each screen pixel column
        for sx in range(ss.screen_width):
            # Iteration constant is current world coordinate
            c = complex(ss.world_x(sx), ss.world_y(sy))
            z = complex(0, 0)
            iter = 0
            # Iterate z while it remains in the radius
            while abs(z) < radius and iter < max_iter:
                z = z**2 + c
                iter += 1
            # Set color using HSV encoding (saturation @ 100%)
            hue = int(360 * iter / max_iter)
            value: int = 100 if iter < max_iter else 0
            clr.hsva = hue, 100, value, 0  # alpha = 0
            ss.set_screen_pixel(sx, sy, clr)
        # Display pixel row after drawing all columns
        ss.flip()


def main():
    ss = SimpleScreen(
        world_rect=((-2.2, -1.51), (1, 1.51)),
        screen_size=(900, 900),
        draw_function=plot_mandelbrot_set,
        title="Mandelbrot Set",
    )
    ss.show()


main()
