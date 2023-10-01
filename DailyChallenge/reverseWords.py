class Solution:
    # reverse the word
    def reverse(self,w):
        return w[::-1]

    def reverseWords(self, s: str) -> str:
        s=s.split() # spliting into elements of array
        for i in range(len(s)):
            s[i]=self.reverse(s[i]) # reversing word
        
        return ' '.join(s) # join arr elements to make a string
