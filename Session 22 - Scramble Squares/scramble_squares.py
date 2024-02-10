# scramble_squares.py

from typing import List, Any


class Tile:
    def __init__(self, id_num, north, east, south, west):
        self.id_num = id_num
        self.rotation = 0
        self.placed = False
        self.bindings = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        # Rotation = 0, no turn = original orientation
        self.bindings[0][0] = north
        self.bindings[0][1] = east
        self.bindings[0][2] = south
        self.bindings[0][3] = west

        # Rotation = 1, one quarter turn counterclockwise
        self.bindings[1][0] = east
        self.bindings[1][1] = south
        self.bindings[1][2] = west
        self.bindings[1][3] = north

        # Rotation = 2, two quarter turns counterclockwise
        self.bindings[2][0] = south
        self.bindings[2][1] = west
        self.bindings[2][2] = north
        self.bindings[2][3] = east

        # Rotation = 3, three quarter turns counterclockwise
        self.bindings[3][0] = west
        self.bindings[3][1] = north
        self.bindings[3][2] = east
        self.bindings[3][3] = south


class Board:
    def __init__(self):
        self.positions: List[Any] = [None] * 9
        self.tiles: List[Any] = [None] * 9

        # TODO: Enter YOUR specific Tile() constructors
        self.tiles[0] = Tile(0, -4, 2, -1, -2)
        self.tiles[1] = Tile(1, 4, -3, -1, -2)
        self.tiles[2] = Tile(2, -4, 2, -3, -1)
        self.tiles[3] = Tile(3, -1, -3, 2, -4)
        self.tiles[4] = Tile(4, 3, -2, 4, 1)
        self.tiles[5] = Tile(5, -4, -2, 3, 1)
        self.tiles[6] = Tile(6, -4, 2, 3, -1)
        self.tiles[7] = Tile(7, -4, 4, -1, 3)
        self.tiles[8] = Tile(8, 1, 2, 3, -3)

    def print(self):
        for i in range(0, 9, 3):
            p1 = self.positions[i]
            p2 = self.positions[i + 1]
            p3 = self.positions[i + 2]
            print(f"{p1.id_num} r {p1.rotation}", end="\t")
            print(f"{p2.id_num} r {p2.rotation}", end="\t")
            print(f"{p3.id_num} r {p3.rotation}")
        print()

    def is_match(self, tile_a, position_b, binding_site):
        tile_b = self.positions[position_b]
        if tile_b is None:
            return True
        if binding_site == 0:
            sum = tile_a.bindings[tile_a.rotation][0]
            sum += tile_b.bindings[tile_b.rotation][2]
        if binding_site == 1:
            sum = tile_a.bindings[tile_a.rotation][1]
            sum += tile_b.bindings[tile_b.rotation][3]
        if binding_site == 2:
            sum = tile_a.bindings[tile_a.rotation][2]
            sum += tile_b.bindings[tile_b.rotation][0]
        if binding_site == 3:
            sum = tile_a.bindings[tile_a.rotation][3]
            sum += tile_b.bindings[tile_b.rotation][1]
        return sum == 0

    def can_place_tile(self, tile, position):
        if position == 0:
            return self.is_match(tile, 1, 1) and self.is_match(tile, 3, 2)
        if position == 1:
            return (
                self.is_match(tile, 2, 1)
                and self.is_match(tile, 4, 2)
                and self.is_match(tile, 0, 3)
            )
        if position == 2:
            return self.is_match(tile, 5, 2) and self.is_match(tile, 1, 3)
        if position == 3:
            return (
                self.is_match(tile, 0, 0)
                and self.is_match(tile, 4, 1)
                and self.is_match(tile, 3, 2)
            )
        if position == 4:
            return (
                self.is_match(tile, 1, 0)
                and self.is_match(tile, 5, 1)
                and self.is_match(tile, 7, 2)
                and self.is_match(tile, 3, 3)
            )
        if position == 5:
            return (
                self.is_match(tile, 2, 0)
                and self.is_match(tile, 8, 2)
                and self.is_match(tile, 4, 3)
            )
        if position == 6:
            return self.is_match(tile, 3, 0) and self.is_match(tile, 7, 1)
        if position == 7:
            return (
                self.is_match(tile, 4, 0)
                and self.is_match(tile, 8, 1)
                and self.is_match(tile, 6, 3)
            )
        if position == 8:
            return self.is_match(tile, 5, 0) and self.is_match(tile, 7, 3)
        return True

    def solve(self, position=0):
        for tile in self.tiles:
            if tile.placed is False:
                for tile.rotation in range(4):
                    if self.can_place_tile(tile, position):
                        tile.placed = True
                        self.positions[position] = tile
                        if position == 8:
                            self.print()
                            return
                        else:
                            self.solve(position + 1)
                        self.positions[position] = None
                        tile.placed = False


def main():
    board = Board()
    board.solve()


main()
