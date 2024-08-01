class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        s=list(s)
        for idx,c in enumerate(s):
            if c in 'aeiouAEIOU':
                vowels.append(idx)

        n=len(vowels)
        m=n//2
        for i in range(m):
            tmp=s[vowels[i]] 
            s[vowels[i]] = s[vowels[n-1-i]]
            s[vowels[n-1-i]] = tmp

        return ''.join(s)
