def signFunc(product):
        if product>0:
            return 1;
        elif product<0:
            return -1;
        elif product==0:
            return 0;

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1;
        for num in nums:
            p*=num;
        return signFunc(p)
    
