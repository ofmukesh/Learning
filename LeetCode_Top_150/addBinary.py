class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        i=len(a)-1
        j=len(b)-1
        ans=""
        while i>=0 and j >= 0:
            if int(a[i])+int(b[j])+c == 2:
                c=1
                ans="0"+ans
            elif int(a[i])+int(b[j])+c == 3:
                c=1
                ans="1"+ans
            else:
                ans=str(int(a[i])+int(b[j])+c)+ans
                c=0
            i-=1
            j-=1

        while i>=0:
            if int(a[i])+c > 1:
                c=1
                ans="0"+ans
            else:
                ans=str(int(a[i])+c)+ans
                c=0
            i-=1

        while j>=0:
            if int(b[j])+c > 1:
                c=1
                ans="0"+ans
            else:
                ans=str(int(b[j])+c)+ans
                c=0
            j-=1

        if c==1:
            ans="1"+ans
            
        return ans
