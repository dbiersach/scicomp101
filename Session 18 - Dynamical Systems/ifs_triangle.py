# ifs_triangle.py

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
    ifs.set_base_frame(0, 0, 30, 30)

    p = 1 / 3

    ifs.add_mapping(0, 0, 15, 0, 0, 15, Color("blue"), p)
    ifs.add_mapping(15, 0, 30, 0, 15, 15, Color("blue"), p)
    ifs.add_mapping(7.5, 15, 22.5, 15, 7.5, 30, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="Sierpinksi Triangle",
    )
    ss.show()


main()
