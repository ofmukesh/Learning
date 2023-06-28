class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph, queue = defaultdict(list), deque([start])
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, i])
            graph[b].append([a, i])
        
        probabilities = [0.0] * n
        probabilities[start] = 1.0
        while queue:
            current = queue.popleft()
            for neighbor, i in graph.get(current, []):
                if probabilities[current] * succProb[i] > probabilities[neighbor]:
                    probabilities[neighbor] = probabilities[current] * succProb[i]
                    queue.append(neighbor)
        
    
        return probabilities[end]
