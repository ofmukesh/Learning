class Solution:
    def makeFancyString(self, s: str) -> str:
        # base case
        if len(s)<3: return s;
        
        # three pointer solution
        i=0;
        j=1;
        k=2;

        while k < len(s):
            if s[i]==s[j]==s[k]:
                s=s[0:k]+s[k+1:]
            else:
                i=j
                j=k
                k+=1
        
        return s
