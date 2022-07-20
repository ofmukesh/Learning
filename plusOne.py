class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)-1;
        i=1;
        while i == 1:
            num = digits[n]+1
            if num==10:
                if n==0:
                    digits.insert(0,1);
                    digits[1]=0;
                    i=0
                else:
                    digits[n]=0;
            else:
                if n==0:
                    digits[0]=num;
                    i=0
                else:
                    digits[n]=num;
                    i=0;
            n=n-1;
        return digits
