import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: # return false if the given number is less than or equal to 0
            return False
        return math.log(n, 4).is_integer()
