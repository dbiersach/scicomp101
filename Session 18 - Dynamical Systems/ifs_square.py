# ifs_square.py

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss) -> None:
    iterations = 200_000
    x = 0.0
    y = 0.0

    # Iterate 100 times, but don't draw any pixels
    # This will give the IFS "time" reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main():
    ifs.set_base_frame(0, 0, 4, 4)

    p = 1 / 4

    ifs.add_mapping(0, 0, 2, 0, 0, 2, Color("blue"), p)
    ifs.add_mapping(2, 0, 4, 0, 2, 2, Color("yellow"), p)
    ifs.add_mapping(0, 2, 2, 2, 0, 4, Color("red"), p)
    ifs.add_mapping(2, 2, 4, 2, 2, 4, Color("green"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((-2, -2), (6, 6)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Square",
    )
    ss.show()


main()
