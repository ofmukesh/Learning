class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafs(root,currLeafs):
            if not root:
                return None
            
            if not root.left and not root.right:
                currLeafs.append(root.val)
            
            getLeafs(root.left,currLeafs)
            getLeafs(root.right,currLeafs)
        
            return currLeafs

        leafs1=getLeafs(root1,[])
        leafs2=getLeafs(root2,[])

        if leafs1!=leafs2:
            return False
        return True

        # time comlpexity -> O(t1+t2)
        # space comlpexity -> O(t1+t2)
