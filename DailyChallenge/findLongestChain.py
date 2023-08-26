class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        
        for pair in pairs:
            if cur < pair[0]: # if curr is smaller then add +1 to answer
                cur = pair[1]
                ans += 1
                
        return ans
