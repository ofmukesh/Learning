class Solution:
    def isCircularSentence(self, s: str) -> bool:
        if len(s)==1: return True
        if s[0]!=s[-1]: return False

        i=0
        j=1
        k=2
        while k<len(s):
            if s[j]==" ":
                if s[i]!=s[k]:
                    return False
            i=j
            j=k
            k+=1

        return True
