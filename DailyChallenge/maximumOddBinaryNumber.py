class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countOne=0
        i=0

        while i<len(s):
            if s[i]=="1":
                s=s[:i]+s[i+1:]
                countOne+=1
                i-=1
            i+=1
        
        # add 1 to last
        s+="1"
        countOne-=1

        # add 1 to top
        for i in range(countOne):
            s="1"+s
        
        return s
