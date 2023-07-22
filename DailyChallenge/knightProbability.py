
from functools import cache

class Solution:
    def __init__(self):
        # Initialize variables to store chessboard size and number of moves
        self.n = 0
        self.k = 0
        # Define the eight possible knight moves as relative coordinates
        self.states = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

    # Helper function to check if given coordinates (x, y) are within chessboard boundaries
    @cache
    def is_valid(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            return True
        return False

    # Function to calculate the probability of knight staying on the board after k moves
    @cache
    def solve(self, x, y, k):
        # Base case: If k is 0, knight is guaranteed to stay on the board
        if k == 0:
            return 1
        rate = 0
        # Loop through all eight possible knight moves
        for dx, dy in self.states:
            n_x, n_y = x + dx, y + dy
            # Check if the new coordinates are valid (within chessboard boundaries)
            if not self.is_valid(n_x, n_y):
                continue
            # Calculate the probability for the current move and add it to the rate
            rate += 0.125 * self.solve(n_x, n_y, k - 1)
        return rate

    # Main function to solve the knight probability problem
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Update the chessboard size and number of moves
        self.n = n
        self.k = k
        # Edge case: If k is 0, simply check if the initial position is valid on the board
        if k == 0:
            return float(self.is_valid(row, column))
        # Otherwise, call the solve function with the starting position and k
        return self.solve(row, column, k)
