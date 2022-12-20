from typing import *
from dataclasses import dataclass

class V(tuple):

    def __new__(cls, x, y) -> Self:
        return super().__new__(cls, (x,y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self: Self, other: Self) -> Self:
        return V(self.x + other.x, self.y + other.y)

    def __sub__(self: Self, other: Self) -> Self:
        return V(self.x - other.x, self.y - other.y)

    def __mul__(self: Self, other) -> Self:
        match other:
            case V(x,y):
                return V(self.x * x, self.y * y)
            case c:
                return V(self.x * c, self.y * c)

    '''
    Neighbors
    '''

    @staticmethod
    def LEFT() -> Self:
        return V(-1,0)

    @staticmethod
    def RIGHT() -> Self:
        return V(1,0)

    @staticmethod
    def UP() -> Self:
        return V(0,-1)

    @staticmethod
    def DOWN() -> Self:
        return V(0,1)

    @staticmethod
    def UL() -> Self:
        return V(-1,-1)

    @staticmethod
    def UR() -> Self:
        return V(1,-1)

    @staticmethod
    def DL() -> Self:
        return V(-1,1)

    @staticmethod
    def DR() -> Self:
        return V(1,1)

    def r(self) -> Self:
        return self + V.RIGHT()

    def l(self) -> Self:
        return self + V.LEFT()

    def u(self) -> Self:
        return self + V.UP()

    def d(self) -> Self:
        return self + V.DOWN()

    def ur(self) -> Self:
        return self + V.UR()

    def ul(self) -> Self:
        return self + V.UL()

    def dr(self) -> Self:
        return self + V.DR()

    def dl(self) -> Self:
        return self + V.DL()

    def neigh_hor(self) -> list[Self]:
        return [self.l(), self.r()]

    def neigh_vert(self) -> list[Self]:
        return [self.u(), self.d()]

    def neigh_straight(self) -> list[Self]:
        return self.neigh_hor() + self.neigh_vert()

    def neigh_diag(self) -> list[Self]:
        return [self.ur(), self.dr(), self.dl(), self.ul()]

    def neigh8(self) -> list[Self]:
        return self.neigh_straight() + self.neigh_diag()

    def neigh9(self) -> list[Self]:
        return self.neigh8() + [self]

    def neigh_square(self, n: int) -> list[Self]:
        return [V(x,y,z) for x in range(self.x - n, self.x + n + 1) for y in range(self.y - n, self.y + n + 1) for z in range(self.z - n, self.z + n + 1)]

    __match_args__ = ('x', 'y')



class V3(tuple):

    def __new__(cls, x, y, z) -> Self:
        return super().__new__(cls, (x,y,z))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        return self[2]

    '''
    Neighbors
    '''

    def r(self) -> Self:
        return V3(self.x+1, self.y, self.z)

    def l(self) -> Self:
        return V3(self.x-1, self.y, self.z)

    def b(self) -> Self:
        return V3(self.x, self.y+1, self.z)

    def f(self) -> Self:
        return V3(self.x, self.y-1, self.z)

    def u(self) -> Self:
        return V3(self.x, self.y, self.z+1)

    def d(self) -> Self:
        return V3(self.x, self.y, self.z-1)

    def ur(self) -> Self:
        return V3(self.x+1, self.y, self.z+1)

    def ul(self) -> Self:
        return V3(self.x-1, self.y, self.z+1)

    def ub(self) -> Self:
        return V3(self.x, self.y+1, self.z+1)

    def uf(self) -> Self:
        return V3(self.x, self.y-1, self.z+1)

    def rb(self) -> Self:
        return V3(self.x+1, self.y+1, self.z)

    def rf(self) -> Self:
        return V3(self.x+1, self.y-1, self.z)

    def rf(self) -> Self:
        return V3(self.x+1, self.y-1, self.z)

    def dr(self) -> Self:
        return V3(self.x+1, self.y, self.z-1)

    def dl(self) -> Self:
        return V3(self.x-1, self.y, self.z-1)

    def neigh_hor(self) -> list[Self]:
        return [self.l(), self.r(), self.f(), self.b()]

    def neigh_vert(self) -> list[Self]:
        return [self.u(), self.d()]

    def neigh_straight(self) -> list[Self]:
        return self.neigh_hor() + self.neigh_vert()

    def neigh_diag(self) -> list[Self]:
        return [self.ur(), self.dr(), self.dl(), self.ul()]

    __match_args__ = ('x', 'y', 'z')
