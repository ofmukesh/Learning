# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        prev=None

        # find middle
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        # remove middle
        if prev:
            prev.next=slow.next
        else:
            head=None

        return head
