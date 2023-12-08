class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        # Step 1: Start with an empty result string
        result = []

        # Step 2: Perform preorder traversal
        self.preorderTraversal(root, result)

        # Step 3: Return the final result string
        return ''.join(result)

    def preorderTraversal(self, node, result):
        if node is None:
            return

        # Step 4: Append the current node's value to the result
        result.append(str(node.val))

        # Step 5: Check if the current node has a left child or a right child
        if node.left is not None or node.right is not None:

            # Step 6: If there is a left child, add empty parentheses for it
            result.append("(")
            self.preorderTraversal(node.left, result)
            result.append(")")

        # Step 7: If there is a right child, process it similarly
        if node.right is not None:
            result.append("(")
            self.preorderTraversal(node.right, result)
            result.append(")")

        # Step 8: The recursion will handle all the child nodes
