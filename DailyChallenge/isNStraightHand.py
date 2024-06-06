#----------------------------------------------------------------------------------Solution 1 (O(n^2) and O(n)-----------------------------------------------------------------------------
# Base Condition:
#    When the cards are not possible to group: if we can't make groups of given groupSize by cards, this condition is possible when some elements are 
#    left after grouping cards. 
 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base conditions
        if len(hand)%groupSize !=0 : return False
        result=[[] for _ in range(len(hand)//groupSize)]
        curr=0
        hand.sort()

        l=len(hand)
        i=0
        while i < l:
            if len(result[curr])==0:
                result[curr].append(hand[i])
                hand.pop(i)
                l-=1
            else:
                if result[curr][-1]+1==hand[i]:
                    result[curr].append(hand[i])
                    hand.pop(i)
                    l-=1
                elif result[curr][-1]==hand[i]:
                    i+=1
                else:
                    return False

            if len(result[curr])==groupSize:
                i=0
                curr+=1
        
        if len(hand)==0:
            return True
        else:
            return False

#----------------------------------------------------------------------------------Solution 1 (O(n^2) and O(1)-----------------------------------------------------------------------------
# Base Condition:
#    When the cards are not possible to group: if we can't make groups of given groupSize by cards, this condition is possible when some elements are 
#    left after grouping cards. 
 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base conditions
        if len(hand)%groupSize !=0 : return False

        # make groups
        last=None
        resultL=0
        hand.sort()

        l=len(hand)
        i=0
        while i < l:
            if resultL==0:
                last=hand[i]
                hand.pop(i)
                l-=1
                resultL+=1
            else:
                if last+1==hand[i]:
                    last=hand[i]
                    hand.pop(i)
                    l-=1
                    resultL+=1
                elif last==hand[i]:
                    i+=1
                else:
                    return False

            if resultL==groupSize:
                i=0
                last=None
                resultL=0
        
        if len(hand)==0:
            return True
        else:
            return False
