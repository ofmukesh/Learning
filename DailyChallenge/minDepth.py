class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.right and not root.left:
            return 1
        elif not root.right: 
            return 1 + self.minDepth(root.left)
        elif not root.left: 
            return 1 + self.minDepth(root.right)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
