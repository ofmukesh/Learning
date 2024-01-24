class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, pathBits) -> int:
        if not root:
            return 0
        
        pathBits ^= (1 << root.val)
        '''
        (1 < root.val) => This is a bitwise left shift operation. 
        It takes the binary representation of the number 1 and shifts it to the left by root.val positions
        example: root.val=3, pathBits=..000000001 
        so after bit operation, pathBits=...000001000
        -------------
        pathBits ^= (1 << root.val) => (^=) is a XOR bit operation.
        if root.val is already present in pathBits, it will be removed; if not, it will be added.
        '''

        if not root.left and not root.right:
            # Check if the path is pseudo-palindromic.
            return 1 if ((pathBits & (pathBits - 1)) == 0)  else 0 

        left_count = self.dfs(root.left, pathBits)
        right_count = self.dfs(root.right, pathBits)


        return left_count + right_count
