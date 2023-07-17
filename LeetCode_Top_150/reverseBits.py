class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Variable to store the reversed bits
        
        for i in range(32):  # We iterate 32 times since an integer in Python has 32 bits
            lsb = n & 1  # Getting the least significant bit (rightmost bit) of n using bitwise AND with 1
            rlsb = lsb << (31 - i)  # Left shifting the least significant bit to its reversed position
            res = res | rlsb  # Setting the corresponding reversed bit in 'res' using bitwise OR
            n = n >> 1  # Right shifting n by 1 to move to the next bit in the original number
        
        return res  # Return the result with reversed bits
