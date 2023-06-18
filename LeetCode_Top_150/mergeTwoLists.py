# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# creating a merged linkedlist of l1 and l2 linkedlist , if current node of l1 is smaller than l2 -> add l1 node to new list
# or if current l2 node is smaller or equal to current l1 node then add l2 node to new merged linked list
# if l1 has no val then add remaining l2 nodes to new list
# or if l2 has no val then add remaining l1 nodes to new list


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode()
        newList=temp

        while l1 and l2:
            if l1.val<l2.val:
                newList.next=l1
                l1=l1.next
            else:
                newList.next=l2
                l2=l2.next
            newList=newList.next

        if not l1:
            newList.next=l2
        elif not l2:
            newList.next=l1

        return temp.next

# Time complexity - O(n)
# Space complexity - O(n)
