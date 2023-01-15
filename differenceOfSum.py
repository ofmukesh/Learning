def getSum(n):
    
    s = 0
    while (n != 0):
       
        s = s + (n % 10)
        n = n//10
       
    return s
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1=0
        s2=0
        for ele in nums:
            s1+=ele;
            s2+=getSum(ele);
        return abs(s1-s2)
            
            
        
