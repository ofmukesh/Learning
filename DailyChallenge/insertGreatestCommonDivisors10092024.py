# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,a, b):
        if (a == 0):
            return b
        if (b == 0):
            return a
        if (a == b):
            return a
        if (a > b):
            return gcd(a-b, b)image.png
        return gcd(a, b-a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        curr=head.next

        while curr:
            new_val=self.gcd(prev.val,curr.val)
            prev.next=ListNode(new_val,curr)
            prev=curr
            curr=curr.next

        return head
