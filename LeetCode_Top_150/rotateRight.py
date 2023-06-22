# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # calculating length of the list
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next

        # return head if k equal to length (no rotations)
        if k==length or k==0 or not head or not head.next or k%length==0:
            return head
        elif k<length:
            k = k
        elif k>length:
            k = k % length
        # Rotate List
        r=length-k #rotation point
        i=1
        leftList=head
        while i<r:
            leftList=leftList.next
            i+=1
        # split List respect to rotation point
        rightList=leftList.next
        leftList.next=None
        
        # join list again
        temp=rightList # temp start pointer of rotated list
        while temp.next:
            temp=temp.next
        temp.next=head

        head=rightList # set head to start point of rotated list
        return head
