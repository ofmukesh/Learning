# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        self.ans=False
        def dfs(root,sum):
            if (not root.left and not root.right) and sum==targetSum:
                self.ans=True
                return 
            if root.left:
                dfs(root.left,sum+root.left.val)
            if root.right:
                dfs(root.right,sum+root.right.val)

        dfs(root,root.val)
        return self.ans
