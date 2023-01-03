class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        for i in str(n):
            p*=int(i)
            s+=int(i)
        return p-s
