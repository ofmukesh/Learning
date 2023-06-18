# using two pointer first left and second right, move right to nth node of given linked list then move both ele to next 
# and when right pointer have null node break it and remove left pointer
# why we will remove left pointer node , think about it 
# let's see when the right node pointer goes at null it means left pointer is on nth node bcz of right pointer starts from nth node

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=0

        while curr:
            l+=1
            curr=curr.next

        if l==n:
            head=head.next if head else None
        i=0
        curr,prev=head,head
        while curr:
            if i==l-n:
                prev.next=curr.next
            prev=curr
            curr=curr.next
            i+=1

        return head

################################# Other Solotion #########################
# using two pointer first left and second right, move right to nth node of given linked list then move both ele to next 
# and when right pointer have null node break it and remove left pointer
# why we will remove left pointer node , think about it 
# let's see when the right node pointer goes at null it means left pointer is on nth node bcz of right pointer starts from nth node

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        l=dummy
        r=head
        
        # right pointer to nth node
        for i in range(n):
            r=r.next
        
        # move left and right both while right not None
        while r:
            r=r.next
            l=l.next
        
        # removing node
        l.next=l.next.next

        return dummy.next
