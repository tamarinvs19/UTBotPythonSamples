from __future__ import annotations
from itertools import product
from typing import List


class MatrixException(Exception):
    def __init__(self, description):
        self.description = description


class Matrix:
    def __init__(self, elements: List[List[float]]):
        self.dim = (
            len(elements),
            max(len(elements[i]) for i in range(len(elements)))
            if len(elements) > 0 else 0
        )
        self.elements = [
            row + [0] * (self.dim[1] - len(row))
            for row in elements
        ]

    def is_diagonal(self) -> bool:
        if self.dim[0] != self.dim[1]:
            raise MatrixException("Bad matrix")

        for i, row in enumerate(self.elements):
            for j, elem in enumerate(row):
                if i != j and elem != 0:
                    return False
        return True

    def plus_one(self) -> None:
        for i, line in enumerate(self.elements):
            for j, elem in enumerate(line):
                self.elements[i][j] = elem + 1


if __name__ == '__main__':
    a = Matrix([[1., 2.]])
    b = Matrix([[3.], [4.]])
    print(a @ b)
