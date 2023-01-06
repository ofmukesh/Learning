"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pre = [] #array
        
        def check(node, arr):
            if node == None: #base call 1
                return 0
            
            arr.append(node.val) #add val to list

            if node.children == None: #base call 2
               return 0
            
            i = 0
            while i < len(node.children): #recursive call
                check(node.children[i], arr)
                i += 1

        check(root, pre)
        return pre
