class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        res = 0

        while q:
            q.pop() # For Alice
            res += q.pop() # For you
            q.popleft() # For Bob
        
        return res
