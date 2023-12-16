class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s)!=len(t):
            return False

        s=sorted(s)
        t=sorted(t)

        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        
        return True

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s)!=len(t):
            return False

        wordsOfS={}

        for word in s:
            wordsOfS[word]=wordsOfS.get(word,0)+1
        
        countOfT=len(t)
        for word in t:
            if wordsOfS.get(word) and wordsOfS[word]!=0:
                wordsOfS[word]-=1
                countOfT-=1
            else:
                return False

        if countOfT!=0:
            return False
        return True

# Time complexity -> O(n), n is length of string s
# Space complexity -> O(s)
'''
