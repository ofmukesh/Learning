class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Swapping same characters
        if s==goal:
            return len(set(s)) != len(goal)

        # find swapping latters 
        i = 0
        j = len(s) - 1
        #ith
        while i < j and s[i] == goal[i]:
            i += 1
        #jth
        while j >= 0 and s[j] == goal[j]:
            j -= 1

        # swapping latters
        tmp=s[i]
        s=s[0:i]+s[j]+s[i+1:]
        s=s[0:j]+tmp+s[j+1:]
        
        if s==goal:
            return True
        return False
            
