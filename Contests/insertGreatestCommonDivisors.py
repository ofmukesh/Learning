# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dump=head
        prev=head
        head=head.next
        
        while head:
            g_c_d=math.gcd(head.val,prev.val)
            prev.next=ListNode(g_c_d)
            prev.next.next=head
            prev=prev.next.next
            head=head.next
        
        return dump
