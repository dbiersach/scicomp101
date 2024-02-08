# mandelbrot_set.py

from simple_screen import SimpleScreen
import pygame
from pygame import Color


def plot_mandelbrot_set(ss):
    max_iter = 100
    radius = 16

    clr = Color(0)

    # For each screen pixel row
    for sy in reversed(range(ss.screen_height)):
        wy: float = ss.world_y(sy)
        # For each screen pixel column
        for sx in range(ss.screen_width):
            # Convert screen coordinates to world coordinates
            # mapping y to the imaginary component of z
            wx: float = ss.world_x(sx)
            zx: float = wx
            zy: float = wy
            zx_2: float = zx * zx
            zy_2: float = zy * zy
            iter = 0
            # Iterate z = z**2 + (original world coordinate)
            while zx_2 + zy_2 < radius and iter < max_iter:
                nx: float = zx_2 - zy_2 + wx
                ny: float = 2 * zx * zy + wy
                zx = nx
                zy = ny
                zx_2 = zx * zx
                zy_2 = zy * zy
                iter += 1
            # Set color using HSV encoding (saturation @ 100%)
            hue = int(360 * iter / max_iter)
            value: int = 100 if iter < max_iter else 0
            clr.hsva = hue, 100, value, 0  # alpha = 0
            ss.set_screen_pixel(sx, sy, clr)
        # Display pixel row after drawing all columns
        ss.flip()


def handle_events(ss, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            wr = ss.world_rects[-1]
            print(
                (
                    f"Current world rectangle: "
                    f"({wr[0][0]:.4f}, {wr[0][1]:.4f}) - "
                    f"({wr[1][0]:.4f}, {wr[1][1]:.4f})"
                )
            )
    return


def main():
    ss = SimpleScreen(
        world_rect=((-2.2, -1.51), (1, 1.51)),
        screen_size=(900, 900),
        draw_function=plot_mandelbrot_set,
        event_function=handle_events,
        title="Mandelbrot Set",
    )

    ss.show()


main()
