class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        i=len(digits)-1
        while c==1 and i>=0:
            if digits[i]+c>9:
                digits[i]=(digits[i]+c)%10
            else:
                digits[i]+=c
                c=0
            i-=1
        if c!=0:
            digits.insert(0,c)
        return digits
            
