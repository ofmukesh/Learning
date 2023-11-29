class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Iterate through each bit in the binary representation
        for i in range(32):
            # Check if the current bit is set
            if n & 1 == 1:
                count += 1

            # Right shift to move to the next bit
            n >>= 1

        return count
