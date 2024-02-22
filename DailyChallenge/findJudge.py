class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trust_map = {}

        for a, b in trust:
            trust_map[a] = -1
            if trust_map.get(b, 0) != -1:
                trust_map[b] = trust_map.get(b, 0) + 1

        for person, trust_count in trust_map.items():
            if trust_count == n - 1:
                return person

        return -1
