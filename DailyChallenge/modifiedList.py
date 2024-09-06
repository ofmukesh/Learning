# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_dict={}
        for num in nums:
            nums_dict[num]=1
        
        prev=None
        curr=head
        while curr:
            if nums_dict.get(curr.val):
                if not prev:
                    prev=None
                    head=head.next
                    curr=curr.next
                else:
                    prev.next=curr.next
                    curr=curr.next
            else:
                prev=curr
                curr=curr.next
        
        return head
