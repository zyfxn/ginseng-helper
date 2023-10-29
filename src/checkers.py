# checkers
from Types import *
from config import standards
from graph import get_graph_cell


def distance_allow(extend: Cell, cur: Cell, limit: int):
    d1 = standards.dmx[extend.x][extend.y]
    d0 = standards.dmx[cur.x][cur.y]
    # little trick to prevent seeking
    if d1 == 1 and d0 != 2:
        d1 = 4
    if limit < d1:
        return False
    return True


def is_inner_bound(cell: Cell):
    b = standards.inb
    if b[0] <= cell.x < b[1] and b[0] <= cell.y < b[1]:
        return True
    return False


def is_outer_bound(cell: Cell):
    b = standards.otb
    if cell.x < 0 or b <= cell.x or cell.y < 0 or b <= cell.y:
        return True
    return False


def root_pass_through(cell: Cell, enter: int):
    if cell.type not in (CellType.ROOT, CellType.ROOT_UNSEEN):
        return False
    if CellType.UNKNOWN in (cell.root.enter, cell.root.leave):
        return True
    if enter in (cell.root.enter, cell.root.leave):
        return True
    return False


def ginseng_reached(extend: Cell, cur: Cell):
    if not is_inner_bound(extend):
        return False
    if cur.root.enter == opposite(cur.root.leave):
        return True
    return False


def ginseng_reached_check(stype: int, step: int):
    rl = standards.len
    if stype == RootType.THICK:
        return step < rl + 1
    elif stype == RootType.BOTH:
        return step == rl + 1
    elif stype in (RootType.THIN, RootType.TAIL):
        return rl + 1 < step < rl + 1 + rl
    return False


def connected(extend: Cell):
    base = get_graph_cell(extend.x, extend.y)
    if base is None:
        return False
    if base.type != CellType.ROOT:
        return False
    # path is empty yet
    if base.root.id == 0:
        return False
    # circle
    if base.root.id == extend.root.id:
        return False
    return root_pass_through(base, extend.root.enter)


def connect_check(stype: int, extend: Cell, step: int):
    base = get_graph_cell(extend.x, extend.y)
    ttype = base.root.type
    rl = standards.len
    if stype == RootType.THICK and ttype > RootType.THICK:
        return False
    elif stype == RootType.BOTH and ttype >= RootType.BOTH:
        return False
    elif stype == RootType.THIN and ttype > RootType.THIN:
        return False
    elif stype in (RootType.THIN, RootType.TAIL):
        if ttype == RootType.BOTH:
            return step <= rl + 1
        elif ttype == RootType.THIN:
            return step <= rl
    return True


def is_unknown_cell(extend: Cell):
    if is_inner_bound(extend):
        return False
    if is_outer_bound(extend):
        return False
    base = get_graph_cell(extend.x, extend.y)
    if base is None:
        return True
    if base.type < 0:
        if base.type == CellType.ROOT_UNSEEN and not root_pass_through(base, extend.root.enter):
            return False
        return True
    if base.type == CellType.ROOT and base.root.id == 0 and root_pass_through(base, extend.root.enter):
        return True
    return False
