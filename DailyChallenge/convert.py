class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s

        res=""
        for r in range(numRows):
            incrmt=(numRows-1) * 2
            for i in range(r,len(s),incrmt):
                # adding next char to res
                res+=s[i] 
                if r>0 and r<numRows-1 and incrmt+i-2 * r < len(s):
                    res+=s[incrmt+i-2 * r]
        return res
