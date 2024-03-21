class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revList=None

        while head:
            temp_next=head.next 
            head.next=revList
            revList=head
            head=temp_next

        return revList

# Time complexity - O(n)
# Space complexity - O(1)
