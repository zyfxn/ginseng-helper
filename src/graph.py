# ginseng graph data
from Types import Cell


def key(x: int, y: int):
    if x < 0 or y < 0:
        raise Exception('key cal error')
    return x * 100 + y


class Graph:
    def __init__(self):
        self.graph: dict[int, Cell] = dict()

    def get(self, x: int, y: int):
        return self.graph.get(key(x, y))

    def set(self, cell: Cell):
        self.graph.setdefault(key(cell.x, cell.y), cell)

    def remove(self, cell: Cell):
        self.graph.pop(key(cell.x, cell.y))


BaseGraph = Graph()
AssumedGraph = Graph()


def get_graph_cell(x: int, y: int) -> Cell | None:
    obj = AssumedGraph.get(x, y)
    if obj is None:
        obj = BaseGraph.get(x, y)
    return obj
