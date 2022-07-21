class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        i=len(s)-1
        while i>=0:
            if s[i]=="":
                i=i-1;
            else:
                return len(s[i])
                break
            
