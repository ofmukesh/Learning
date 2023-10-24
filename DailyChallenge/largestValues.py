# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Define a recursive DFS function
        def dfs(node, level):
            # If the current node is None (base case), return
            if not node:
                return

            # Check if the current level is equal to the length of the result list
            if level == len(res):
                # If so, add a new element to the result list with the node's value
                res.append(node.val)
            else:
                # If the level already exists in the result list, update it with the maximum value
                res[level] = max(res[level], node.val)

            # Recursively call the dfs function for the left and right children of the node
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        # Initialize the result list
        res = []
        # Start DFS from the root node at level 0
        dfs(root, 0)

        # Return the list of maximum values at each level of the tree
        return res
