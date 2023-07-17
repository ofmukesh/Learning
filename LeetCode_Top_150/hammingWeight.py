class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        #1 by using & bit operator, we will simply remove 1's one by one
        while n:
            n &= (n-1)
            res += 1

        #2 Basically we were doing here is cheking last bit is 0 or 1 then shifting right it
        # while n:
        #     res += (n % 2)
        #     n=n>>1
        
        return res


#Time compexity O(32) > O(1)
#Space compexity O(1)
