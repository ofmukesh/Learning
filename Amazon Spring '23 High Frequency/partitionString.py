class Solution:
    def partitionString(self, s: str) -> int:
        curr_hash={}
        l=1

        for c in s:
            if curr_hash.get(c):
                curr_hash={}
                l+=1
            curr_hash[c]=1
        
        return l
