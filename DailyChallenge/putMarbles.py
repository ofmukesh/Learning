class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        ans = 0
        ans1 = 0
        k -= 1
        res1 = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        res = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        res1.sort(reverse=True)
        res.sort()
        for i in range(k):
            ans1 += res1[i]
        for i in range(k):
            ans += res[i]
        return (ans1 - ans)
