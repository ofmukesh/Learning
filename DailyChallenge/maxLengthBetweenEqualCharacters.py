class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        charIndexs={}
        ans=-1

        for i,char in enumerate(s):
            if charIndexs.get(char)!=None:
                ans=max(ans,i-charIndexs[char]-1)
            else:
                charIndexs[char]=i
        
        return ans
