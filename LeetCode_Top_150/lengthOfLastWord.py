class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)
        count=0

        for i in range(l-1,-1,-1):
            # return length of last world before next word starts
            if s[i]==' ' and count>0:
                return count
            
            if s[i]!=' ':
                count+=1
        return count
