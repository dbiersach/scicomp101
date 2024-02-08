# ifs_bnl.py

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 500_000
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
    ifs.set_base_frame(0, 0, 17, 7)

    p = 1 / 29

    ifs.add_mapping(0, 6, 2, 6, 0, 7, Color("lightblue"), p)  # 01
    ifs.add_mapping(2, 6, 4, 6, 2, 7, Color("blue"), p)  # 02
    ifs.add_mapping(1, 4, 1, 6, 0, 4, Color("blue"), p)  # 03
    ifs.add_mapping(4, 6, 4, 4, 5, 6, Color("blue"), p)  # 04
    ifs.add_mapping(0, 3, 2, 3, 0, 4, Color("blue"), p)  # 05
    ifs.add_mapping(4, 4, 2, 4, 4, 3, Color("red"), p)  # 06
    ifs.add_mapping(1, 1, 1, 3, 0, 1, Color("pink"), p)  # 07
    ifs.add_mapping(4, 3, 4, 1, 5, 3, Color("blue"), p)  # 08
    ifs.add_mapping(0, 0, 2, 0, 0, 1, Color("blue"), p)  # 09
    ifs.add_mapping(4, 1, 2, 1, 4, 0, Color("sienna"), p)  # 10

    ifs.add_mapping(6, 6, 7, 6, 6, 7, Color("blue"), p)  # 11
    ifs.add_mapping(10, 6, 11, 6, 10, 7, Color("papayawhip"), p)  # 12
    ifs.add_mapping(6, 5, 8, 5, 6, 6, Color("chartreuse"), p)  # 13
    ifs.add_mapping(11, 4, 11, 6, 10, 4, Color("blue"), p)  # 14
    ifs.add_mapping(7, 3, 7, 5, 6, 3, Color("blue"), p)  # 15
    ifs.add_mapping(8, 4, 9, 4, 8, 5, Color("blue"), p)  # 16
    ifs.add_mapping(7, 1, 7, 3, 6, 1, Color("orange"), p)  # 17
    ifs.add_mapping(9, 2, 9, 4, 8, 2, Color("blue"), p)  # 18
    ifs.add_mapping(10, 4, 10, 2, 11, 4, Color("maroon"), p)  # 19
    ifs.add_mapping(6, 0, 7, 0, 6, 1, Color("blue"), p)  # 20
    ifs.add_mapping(9, 1, 11, 1, 9, 2, Color("blue"), p)  # 21
    ifs.add_mapping(10, 0, 11, 0, 10, 1, Color("yellow"), p)  # 22

    ifs.add_mapping(13, 5, 13, 7, 12, 5, Color("green"), p)  # 23
    ifs.add_mapping(12, 4, 13, 4, 12, 5, Color("blue"), p)  # 24
    ifs.add_mapping(12, 4, 12, 2, 13, 4, Color("blue"), p)  # 25
    ifs.add_mapping(13, 1, 13, 2, 12, 1, Color("white"), p)  # 26
    ifs.add_mapping(12, 0, 14, 0, 12, 1, Color("blue"), p)  # 27
    ifs.add_mapping(15, 0, 15, 1, 14, 0, Color("blue"), p)  # 28
    ifs.add_mapping(15, 0, 17, 0, 15, 1, Color("purple"), p)  # 29

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (17, 7)),
        screen_size=(1200, 500),
        draw_function=plot_ifs,
        title="Brookhaven National Laboratory",
    )
    ss.show()


main()
