class Solution:
    def trailingZeroes(self, n: int) -> int:
        a=5
        count_zero=0
        while (a)<=n:
            count_zero+=n//a
            a=a*5
        return count_zero
