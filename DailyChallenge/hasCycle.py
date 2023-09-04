# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# try to solve the question using two pointer method slow and fast,
# forward slow pointer to next node and fast pointer to next of next node, while fast node pointer is not None
# if slow and fast found at same node return True , bcz if linked list has cycle then at a condition slow and fast pointer comes on same node
# if fast or slow have no next (next is None) then return False bcz the linked list has no cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return false if LinkedList is empty
        if not head:
            return False

        # starting slow from head
        slow=head

        # starting fast from next of head
        fast=head.next

        while fast and fast.next:

            # if slow and fast found at same node return True
            if slow==fast:
                return True

            # slow -> slow.next
            slow=slow.next

            # fast -> fast.next.next
            fast=fast.next.next
            

        return False
        

# Time complexity - o(n)
# Space complexity - o(1)
