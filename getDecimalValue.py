# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=0;
        temp=1;
        arr=[]
        while head:
            arr=[head.val]+arr;
            head=head.next;
        for val in arr:
            res+=val*temp;
            temp*=2;
        return res
