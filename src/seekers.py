# seekers
from Types import Direct, Cell, CellType, cell_extend
from checkers import ginseng_reached, is_unknown_cell, distance_allow
from config import standards
from graph import AssumedGraph, get_graph_cell


class SeekerStatus:
    CONTINUE = 0
    ROLLBACK = 1
    FINISH = 2


class SeekerMode:
    THICK = 0
    THIN = 1


class Seeker:
    extend: Cell = None

    def __init__(self, cur: Cell, limit: int, step: int, mode: int):
        if cur.type is not CellType.ROOT:
            raise Exception('Seeker is not root')
        self.cur = cur
        self.base = get_graph_cell(self.cur.x, self.cur.y)
        self.limit = limit
        self.step = step
        self.mode = mode
        self.direct_options = self.__make_direct_options()
        self.direct_options_len: int = len(self.direct_options)
        self.di = -1

    def __make_direct_options(self):
        enter = self.cur.root.enter
        if self.base is not None and self.base.type in (CellType.ROOT_UNSEEN, CellType.ROOT):
            opt = [self.base.root.enter, self.base.root.leave]
        else:
            opt = [Direct.UP, Direct.RIGHT, Direct.DOWN, Direct.LEFT]
        if enter not in opt:
            raise Exception('generate leave direct error')
        for i in range(4):
            if opt[0] == enter:
                opt.pop(0)
                break
            d0 = opt.pop(0)
            opt.append(d0)
        return opt

    def __save(self):
        AssumedGraph.set(self.cur)

    def __remove(self):
        AssumedGraph.remove(self.cur)

    def next(self) -> int:
        # not first time
        if 0 <= self.di < self.direct_options_len:
            self.__remove()
        for self.di in range(self.di + 1, self.direct_options_len):
            self.cur.root.leave = self.direct_options[self.di]
            self.extend = cell_extend(self.cur, CellType.ROOT, self.cur.root.leave)
            if ginseng_reached(self.extend, self.cur):
                if self.mode == SeekerMode.THICK or self.step > standards.thick_len + 1:
                    self.__save()
                    return SeekerStatus.FINISH
            elif is_unknown_cell(self.extend) and \
                    distance_allow(self.extend, self.cur, self.limit - 1) and self.limit > 1:
                self.__save()
                return SeekerStatus.CONTINUE
        self.di = self.direct_options_len
        return SeekerStatus.ROLLBACK


def get_next_seeker(seeker: Seeker):
    return Seeker(seeker.extend, seeker.limit - 1, seeker.step + 1, SeekerMode.THIN)


if __name__ == '__main__':
    c0 = Cell(1, 1, 1)
    c0.root.enter = 3
    s = Seeker(c0, 8, 1, SeekerMode.THIN)
    print(s.next())
    print(s.next())
    print(s.next())
    print(s.next())
    print(s.next())
