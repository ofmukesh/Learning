def sqrt(n):
    if n < 2:
        return n
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return high

class Solution:
    def mySqrt(self, x: int) -> int:
        return sqrt(x)
