class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]

        for s in strs:
            i=0
            t=""
            while i<len(s) and i<len(ans) and s[i]==ans[i]:
                t+=ans[i]
                i+=1
            ans=t
        
        return ans
