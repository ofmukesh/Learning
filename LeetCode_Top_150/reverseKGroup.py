class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_group = dummy
        while head:
            j, group_end = 1, head #start of group = end after reverse
            while j < k and head.next:
                head = head.next 
                j+=1
            group_start = head #end of group = start after reverse
            next_group = head = head.next #start of next group

            if j != k:  #don't need reverse (not enough nodes)
                break
            #reverse current group without links to prev and next groups
            prev, cur = None, group_end
            while cur != next_group:
                cur.next, cur, prev = prev, cur.next, cur  

            prev_group.next = group_start
            prev_group = group_end
            group_end.next = next_group

        return dummy.next

        
