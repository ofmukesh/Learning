"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            curr=head
            while curr:
                nextNode=curr.next
                curr.next=ListNode(curr.val)
                curr.next.next=nextNode
                curr=nextNode

            curr=head
            while curr:
                if curr.next:
                    curr.next.random=curr.random.next if curr.random else None
                curr=curr.next.next

            copy=head.next
            temp=copy
            while temp:
                temp.next=temp.next.next if temp.next else None
                temp=temp.next

            return copy
        else:
            return head
