class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        s=[w for w in s]

        for word in s:
            if word in "aeiouAEIOU":
                vowels.append(word)
        
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i]=vowels.pop()
        
        return "".join(s)
