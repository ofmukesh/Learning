class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            start >>= 1
            goal >>= 1
        return count
