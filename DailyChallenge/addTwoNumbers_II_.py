# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse linked list
        reversed_list=None
        while l1:
            tmp=l1.next
            l1.next=reversed_list
            reversed_list=l1
            l1=tmp

        # reverse linked list
        reversed_list2=None
        while l2:
            tmp=l2.next
            l2.next=reversed_list2
            reversed_list2=l2
            l2=tmp
        
        # now reversed_list + reversed_list2
        l1=reversed_list
        l2=reversed_list2
        c=0
        while l1 and l2:
            l1.val+=l2.val+c
            
            if l1.val>9:
                l1.val=l1.val-10
                c=1
            else:
                c=0

            # if l1 ends and l2 has remains, then add new node to l1 
            if (not l1.next) and l2.next:
                l1.next=ListNode(0)
            # if l2 ends and la has remains, then add new node to l1 
            elif (not l2.next) and l1.next:
                l2.next=ListNode(0)
            # if carry c has value 1 and both lists pointer are None then add c to sum list (l1)
            elif (not l2.next) and (not l2.next) and c: 
                l1.next=ListNode(c)

            l1=l1.next
            l2=l2.next

        # reverse linked list
        l1=None
        while reversed_list:
            tmp=reversed_list.next
            reversed_list.next=l1
            l1=reversed_list
            reversed_list=tmp
        return l1
