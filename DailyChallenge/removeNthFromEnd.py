# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of the given linked list
        l=0
        node=head
        while node:
            l+=1
            node=node.next
        
        # find target
        target=l-n+1
        if target==1:
            return head.next # return head's next element if target is first element
        else:
            i=1
            prev=None
            node=head
            while i!=target:
                prev=node
                node=node.next
                i+=1
            
            # find and remove n'th node
            prev.next=node.next
            return head
