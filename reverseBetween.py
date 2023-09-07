curr=head
        rightList,leftList,middle=None,None,None

        i=1
        while curr:
            if i==left-1:
                leftList=curr
            if i==left:
                middle=curr
            if i==right:
                nextNode=curr.next
                curr.next=None
                rightList=nextNode
            curr=curr.next
            i+=1

        prev = rightList
        while(middle is not None):
            nxt = middle.next
            middle.next = prev
            prev = middle
            middle = nxt
            
        if leftList:
            leftList.next=prev
        if not leftList:
            return prev
        return head
