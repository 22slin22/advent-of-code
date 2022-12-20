from utils.points import *
from typing import *

T = TypeVar('T')

class Grid:
    def __init__(self, grid: Iterable[Iterable[T]] = None):
        if grid is not None:
            self.grid = list(list(row) for row in grid)
        else:
            self.grid = []

    @property
    def height(self):
        return len(self.grid)

    @property
    def width(self):
        return 0 if len(self.grid) == 0 else len(self.grid[0])

    @property
    def points(self) -> list[list[V]]:
        return [V(x,y) for x in range(self.width) for y in range(self.height)]

    def add_row(self, row):
        self.grid.append(row)

    def __getitem__(self, indices):
        match indices:
            case V(x, y):
                return self.grid[y][x]
            case _:
                return self.grid.__getitem__(indices)

    def __repr__(self) -> str:
        return '\n'.join(str(row) for row in self.grid)

    def __contains__(self, point: V) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def filter_contains(self, points: Iterable[V]) -> list[V]:
        return [p for p in points if p in self]

    def neigh_straight_of(self, point: V) -> list[V]:
        return self.filter_contains(point.neigh_straight())

    def neigh_diag_of(self, point: V) -> list[V]:
        return self.filter_contains(point.neigh_diag())

    def neigh8_of(self, point: V) -> list[V]:
        return self.filter_contains(point.neigh8())
    
    def neigh9_of(self, point: V) -> list[V]:
        return self.filter_contains(point.neigh9())

    def neigh_square_of(self, point: V, n: int) -> list[V]:
        return self.filter_contains(point.neigh_square(n))

    def line_x(self, y: int) -> list[V]:
        return [V(x, y) for x in range(self.width)]

    def line_y(self, x: int) -> list[V]:
        return [V(x, y) for y in range(self.height)]

    def diagonal_down_through(self, point: V) -> list[V]:
        x, y = point
        return [V(x+n, y+n) for n in range(max(-x, -y), min(self.width - x, self.height - y))]

    def diagonal_up_through(self, point: V) -> list[V]:
        x, y = point
        return [V(x+n, y-n) for n in range(max(-x, y-self.height+1), min(self.width - x, y+1))]

    def ray(self, point: V, direction: V, include_start: bool = False):
        ray = [point] if include_start else []
        cur = point + direction

        while cur in self:
            ray.append(cur)
            cur += direction

        return ray

    def rays(self, point: V, directions: Iterable[V] = [V.UP(), V.RIGHT(), V.DOWN(), V.LEFT()], include_start: bool = False) -> list[list[V]]:
        return [self.ray(point, dir, include_start) for dir in directions]

