# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        def sol(node,i):
            if not node:
                return 
            
            try:
                ans[i]=max(ans[i],node.val)
            except:
                ans.append(node.val)
            
            sol(node.left,i+1)
            sol(node.right,i+1)
        
        sol(root,0)
        return ans 
