# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=1;
        c=head;
        while c:
            l+=1;
            c=c.next;

        middle=int(l/2);
        if l%2!=0:
            middle+=1;

        i=1;
        while i!=middle:
            head=head.next;
            i+=1;

        return head
