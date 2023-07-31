# jenga_15.py


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class BlockList:
    def __init__(self):
        self.blocks = []
        _center_x = 0.0
        _center_y = 0.0

    @property
    def size(self):
        return len(self.blocks)

    @property
    def center_x(self):
        return self._center_x

    @property
    def center_y(self):
        return self._center_y

    def calc_center(self):
        sx, sy = 0.0, 0.0
        for block in self.blocks:
            sx = sx + block.x
            sy = sy + block.y
        self._center_x = sx / self.size
        self._center_y = sy / self.size

    def add_block(self, x, y):
        self.blocks.append(Block(x, y))
        self.calc_center()

    def move_blocks(self, delta_x, delta_y):
        for block in self.blocks:
            block.move(delta_x, delta_y)
        self.calc_center()


# Create an empty block list
block_list = BlockList()

# Place initial ensemble
block_list.add_block(7.5, 1.5)
block_list.add_block(1.5, 10.5)


while block_list.center_x < 15:
    print(
        f"Blocks: {block_list.size:>2}"
        f"  Center X: {block_list.center_x:>6.2f}"
        f"  Center Y: {block_list.center_y:>6.2f}"
    )

    # Make room for next ensemble
    block_list.move_blocks(3, 3)

    # Place next ensemble
    block_list.add_block(7.5, 1.5)
    block_list.add_block(1.5, 10.5)
