import unittest
from typing import List, Optional


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        self.prefix_sums = [[0] * col for _ in range(row)]

        for r in range(row):
            sum_ = 0
            for c in range(col):
                sum_ += matrix[r][c]
                self.prefix_sums[r][c] = sum_

        for c in range(col):
            sum_ = 0
            for r in range(row):
                sum_ += self.prefix_sums[r][c]
                self.prefix_sums[r][c] = sum_

    def sumRegion(self, row1, col1, row2, col2):
        a = self.prefix_sums[row2][col2]
        b = self.prefix_sums[row1 - 1][col2] if row1 > 0 else 0
        c = self.prefix_sums[row2][col1 - 1] if col1 > 0 else 0
        d = self.prefix_sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return a - b - c + d


class Test(unittest.TestCase):
    def test1(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        num_matrix = NumMatrix(matrix)
        self.assertIs(num_matrix.sumRegion(*[2, 1, 4, 3]), 8)
        self.assertIs(num_matrix.sumRegion(*[1, 1, 2, 2]), 11)
        self.assertIs(num_matrix.sumRegion(*[1, 2, 2, 4]), 12)

    def test2(self):
        matrix = [
            [3, 0, 1],
            [5, 6, 3],
            [1, 2, 0],
        ]
        num_matrix = NumMatrix(matrix)
        self.assertIs(num_matrix.sumRegion(*[0, 0, 2, 2]), 21)
        self.assertIs(num_matrix.sumRegion(*[1, 1, 2, 2]), 11)


if __name__ == "__main__":
    unittest.main()
