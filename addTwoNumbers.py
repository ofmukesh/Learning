# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode(None);
        node=new;
        t=0;
        while l1 or l2:
            s=0
            if l1 and l2:
                s=l1.val+l2.val+t;
                l1=l1.next;
                l2=l2.next;
            elif l1:
                s=l1.val+t;
                l1=l1.next;
            elif l2:
                s=l2.val+t;
                l2=l2.next;

            if s>9:
                s=s-10
                t=1
            else:
                t=0
            if node.val==None:
                node.val=s
            else:
                node.next=ListNode(s)
                node=node.next
        if t==1:
            node.next=ListNode(t)
            
                
        return new

            
