class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c=0;
        ans="";
        i=0;
        while i<len(word1) or i<len(word2):
            if i>=len(word1):
                ans+=word2[i:len(word2)];
                break;
            elif i>=len(word2):
                ans+=word1[i:len(word1)];
                break;
            if c%2==0:
                ans+=word1[i];
            else:
                ans+=word2[i];
                i+=1;
            c+=1;
        return ans;
