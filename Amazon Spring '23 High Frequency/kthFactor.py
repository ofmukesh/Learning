class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        final = 0
        for x in range(1,n+1):
            if n % x == 0 :
                final += 1 
                if final == k:
                    return x 
        return -1 
