# checkers
from Types import Cell, opposite
from config import standards
from graph import get_graph_cell


def distance_allow(cur: Cell, pre: Cell, limit: int):
    d1 = standards.distance_matrix[cur.x][cur.y]
    d0 = standards.distance_matrix[pre.x][pre.y]
    # little trick to prevent seeking
    if d1 == 1 and d0 != 2:
        d1 = 4
    if limit < d1:
        return False
    return True


def is_inner_bound(cell: Cell):
    bound = standards.inner_bound
    if bound[0] <= cell.x < bound[1] and bound[0] <= cell.y < bound[1]:
        return True
    return False


def is_outer_bound(cell: Cell):
    if cell.x < 0 or standards.outer_bound <= cell.x or cell.y < 0 or standards.outer_bound <= cell.y:
        return True
    return False


def cell_have_there_ways(cell: Cell, enter: int):
    if cell.root.enter is not None and cell.root.leave is not None and \
            cell.root.enter != enter and cell.root.leave != enter:
        return True
    return False


def ginseng_reached(extend: Cell, cur: Cell):
    if not is_inner_bound(extend):
        return False
    if cur.root.enter == opposite(cur.root.leave):
        return True
    return False


def is_unknown_cell(cur: Cell):
    if is_inner_bound(cur):
        return False
    if is_outer_bound(cur):
        return False
    base = get_graph_cell(cur.x, cur.y)
    if base is None or base.type < 0:
        return True
    return False
