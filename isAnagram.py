class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s);
        t=list(t);
        i=0;
        while i<len(t):
            if t[i] in s:
                s.remove(t[i]);
                t.pop(i);
            else:    
                i+=1;
        
        return len(s)==0 and len(t)==0;
# this is a solution for the question but it need an implement.
