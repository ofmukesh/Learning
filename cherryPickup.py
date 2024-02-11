class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2

            if not (0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N) or \
               grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            if r1 == c1 == r2 == N - 1:
                return grid[r1][c1]
   
            if memo[r1][c1][r2] is not None:
                return memo[r1][c1][r2]

            cherries = grid[r1][c1] + (r1 != r2) * grid[r2][c2]

            cherries += max(
                dp(r1 + 1, c1, r2 + 1),
                dp(r1 + 1, c1, r2),
                dp(r1, c1 + 1, r2 + 1),
                dp(r1, c1 + 1, r2)
            )

            memo[r1][c1][r2] = cherries
            return cherries

        return max(0, dp(0, 0, 0))
