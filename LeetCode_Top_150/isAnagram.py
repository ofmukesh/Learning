# Solution 1
# Sort given strings and match elements of these strings is same or not 
# return False if not matched else return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
            
        s=sorted(s)
        t=sorted(t)
        for i in range(len(s)):
            if(s[i]!=t[i]):
                return False
        return True

# Time Complexity:- O(n log n)
# Space Complexity:- O(1)


# Solution 2
# store the frequency of elements of one string and compare the frequency with 2nd string
# if the frequency are not same return False otherwise True  
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        temp={}

        for num in s:
            if temp.get(num)!=None:
                temp[num]+=1
            else:
                temp[num]=1

        for num in t:
            if temp.get(num)==None:
                return False
            else:
                if temp[num]<=0:
                    return False
                else:
                    temp[num]-=1

        return True
# Time Complexity:- O(n)
# Space Complexity:- ( O(n) <= 26 ) --> O(1)
