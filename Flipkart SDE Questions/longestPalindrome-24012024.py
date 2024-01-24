# check left to right at every point in the string
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            # for odd len
            j,k=i,i
            while j>=0 and k<len(s) and s[j]==s[k]:
                if k-j+1>resLen:
                    resLen=k-j+1
                    res=s[j:k+1]
                
                j-=1
                k+=1
            
            # for even len
            j,k=i,i+1
            while j>=0 and k<len(s) and s[j]==s[k]:
                if k-j+1>resLen:
                    resLen=k-j+1
                    res=s[j:k+1]
                
                j-=1
                k+=1

        return res
