# ifs_fern.py

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
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
    ifs.set_base_frame(0, 0, 48, 48)

    ifs.add_mapping(24, 0, 24, 0, 24, 10, Color("green"), 0.01)
    ifs.add_mapping(20, 4, 28, 17.5, 6, 12, Color("green"), 0.07)
    ifs.add_mapping(20.5, 14, 28, -1, 35, 22.5, Color("green"), 0.07)
    ifs.add_mapping(4, 12.5, 44, 9, 7.5, 53, Color("green"), 0.85)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((-5, -5), (55, 65)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="Barnsley Fern",
    )
    ss.show()


main()
