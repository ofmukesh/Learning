class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Define a helper function 'find' to find the representative (root) of a set using path compression.
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])  # Path compression: Set the parent to the root.
            return parent[x]

        # Define a helper function 'union' to unite two sets by setting one's root as the parent of the other's root.
        def union(parent, x, y):
            parent[find(parent, x)] = find(parent, y)  # Set root of 'x' as parent of root of 'y'.

        # Get the number of points in the input.
        n = len(points)

        # Create a list 'edges' to store the edges between points along with their Manhattan distances.
        # This list comprehensively computes the distances between all pairs of points and stores them.
        edges = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for i in range(n) for j in range(i + 1, n)]

        # Sort the edges by their distances in ascending order.
        edges.sort()

        # Create a 'parent' list initialized such that each point is its own parent (initially isolated).
        parent = list(range(n))

        # Initialize 'min_cost' to track the total minimum cost, and 'num_edges' to track the number of edges added to the MST.
        min_cost, num_edges = 0, 0

        # Iterate through the sorted edges.
        for cost, u, v in edges:
            # Check if adding this edge (connecting points 'u' and 'v') doesn't create a cycle in the minimum spanning tree.
            if find(parent, u) != find(parent, v):
                # If it doesn't create a cycle, unite the sets containing 'u' and 'v', and update 'min_cost'.
                union(parent, u, v)
                min_cost += cost
                num_edges += 1
            # If we have added 'n - 1' edges (forming a spanning tree), exit the loop.
            if num_edges == n - 1:
                break

        # Return the minimum cost to connect all points (the minimum spanning tree cost).
        return min_cost
