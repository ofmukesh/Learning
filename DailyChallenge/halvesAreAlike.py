class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels={'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}

        halfLen=len(s)//2
        count=0
        for i in range(len(s)):
            add=0
            if i<halfLen:
                add+=1
            else:
                add-=1
            if vowels.get(s[i]):
                count+=add
        
        return count==0
            
