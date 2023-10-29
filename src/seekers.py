# seekers
from checkers import *
from graph import AssumedGraph, get_graph_cell


class SeekerStatus:
    CONTINUE = 0
    ROLLBACK = 1
    FINISH = 2


class Seeker:
    extend: Cell = None

    def __init__(self, cur_cell: Cell, limit: int, step: int, mode: int):
        if cur_cell.type is not CellType.ROOT:
            raise Exception('Seeker is not root')
        self.cur = cur_cell
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
            opt = []
            if self.base.root.enter != RootType.UNKNOWN:
                opt.append(self.base.root.enter)
            if self.base.root.leave != RootType.UNKNOWN:
                opt.append(self.base.root.leave)
            if len(opt) == 1 and enter in opt:
                opt = [Direct.UP, Direct.RIGHT, Direct.DOWN, Direct.LEFT]
            elif len(opt) == 2 and enter not in opt:
                raise Exception('cell have three ways')
        else:
            opt = [Direct.UP, Direct.RIGHT, Direct.DOWN, Direct.LEFT]
        opt.remove(enter)
        return opt

    def __save(self):
        self.cur.root.leave = self.direct_options[self.di]
        AssumedGraph.set(self.cur)

    def __remove(self):
        AssumedGraph.remove(self.cur)

    def next(self) -> int:
        # not first time
        if 0 <= self.di < self.direct_options_len:
            self.__remove()
        for self.di in range(self.di + 1, self.direct_options_len):
            self.cur.root.leave = self.direct_options[self.di]
            self.extend = cell_extend(self.cur, self.cur.root.leave)
            if ginseng_reached(self.extend, self.cur) and ginseng_reached_check(self.mode, self.step + 1):
                self.__save()
                return SeekerStatus.FINISH
            elif connected(self.extend) and connect_check(self.mode, self.extend, self.step + 1):
                self.__save()
                return SeekerStatus.FINISH
            elif is_unknown_cell(self.extend) and \
                    distance_allow(self.extend, self.cur, self.limit - 1):
                self.__save()
                return SeekerStatus.CONTINUE
        self.di = self.direct_options_len
        return SeekerStatus.ROLLBACK


def get_next_seeker(seeker: Seeker) -> Seeker:
    return Seeker(seeker.extend, seeker.limit - 1, seeker.step + 1, seeker.mode)
