class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            f=False
            n=len(word)
            for i in range((n//2)):
                if word[i]==word[n-i-1]:
                    f=True
                else:
                    f=False
                    break
            
            if len(word)==1 or f==True:
                return word
        
        return ""
