# ginseng basic data structure


class Direct:
    UNKNOWN = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    NONE = 4


def opposite(d: int):
    if d == Direct.UP:
        return Direct.DOWN
    elif d == Direct.DOWN:
        return Direct.UP
    elif d == Direct.LEFT:
        return Direct.RIGHT
    elif d == Direct.RIGHT:
        return Direct.LEFT
    else:
        raise Exception("opposite direction error")


class CellType:
    ROOT_UNSEEN = -3
    SOMETHING = -2
    UNKNOWN = -1
    EMPTY = 0
    ROOT = 1
    STONE = 2


class RootType:
    UNKNOWN = -1
    THICK = 0
    THIN = 1
    BOTH = 2


class Root:
    type: int = RootType.UNKNOWN
    enter: int = Direct.UNKNOWN
    leave: int = Direct.UNKNOWN
    thicker: bool = None  # enter is thicker than leave


class Cell:
    root: Root = Root()
    step: int = 0

    def __init__(self, cell_type: int, x: int, y: int):
        self.type = cell_type
        self.x = x
        self.y = y

    def move(self, to: int):
        if to == Direct.UP:
            self.y += 1
        elif to == Direct.RIGHT:
            self.x += 1
        elif to == Direct.DOWN:
            self.y -= 1
        elif to == Direct.LEFT:
            self.x -= 1
        else:
            raise Exception('move error')


def cell_extend(src: Cell, cell_type: int, to: int) -> Cell:
    res = Cell(cell_type, src.x, src.y)
    res.move(to)
    res.root.enter = opposite(to)
    return res
