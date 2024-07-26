class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        f=True if x<0 else False
        x=abs(x)
        while x>0:
            rev=(rev*10)+(x%10)
            x=x//10

        res=(rev - (rev*2)) if f else rev
       
        return res if (-2**31) <= res <= (2**31) else 0
