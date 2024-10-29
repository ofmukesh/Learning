from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def res(i, j):
            curr = grid[i][j]
            # Calculate possible moves in three directions if within bounds
            if i+1 < len(grid) and j+1 < len(grid[i]) and grid[i+1][j+1] > curr:
                m1 = 1 + answers[i+1][j+1]
            else:
                m1 = 0

            if j+1 < len(grid[i]) and grid[i][j+1] > curr:
                m2 = 1 + answers[i][j+1]
            else:
                m2 = 0

            if i-1 >= 0 and j+1 < len(grid[i]) and grid[i-1][j+1] > curr:
                m3 = 1 + answers[i-1][j+1]
            else:
                m3 = 0

            return max(m1, m2, m3)

        # Initialize the DP table to store max moves from each cell
        answers = [[0] * len(row) for row in grid]
        m, n = len(grid), len(grid[0])

        # Fill answers from right to left
        for j in range(n-1, -1, -1):
            for i in range(m):
                answers[i][j] = res(i, j)

        # Find the maximum number of moves starting from any cell in the first column
        ans = max(row[0] for row in answers)
        return ans
