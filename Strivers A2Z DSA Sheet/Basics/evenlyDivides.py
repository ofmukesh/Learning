class Solution:
    def evenlyDivides (self, N):
        c=0
        dup=N
        while N!=0:
            if (N%10)!=0 and  (dup % (N%10)) ==0:
                c+=1
            N=N//10
        return c
