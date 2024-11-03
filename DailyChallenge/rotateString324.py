class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal: return True;

        for i in range(len(s)):
            c=s[0]
            s=s[1:]+c
            if s==goal:
                return True

        return False
