class Solution: # DFS Approach
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and dfs(t1.left,t2.left) and dfs(t1.right, t2.right)
        return dfs(p,q)
