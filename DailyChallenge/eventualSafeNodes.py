class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited, res = [-1] * n, []
        def explore(u):
            visited[u] = 0
            for v in graph[u]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
            
            visited[u] = 1
            res.append(u)
            return False

        for u in range(n):
            if visited[u] == -1: explore(u)

        return sorted(res)
