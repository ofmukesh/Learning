class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        else:
            s=1 # intialize variable =1 for array sum
            ans=[1] # arr
            for i in range(1,n):
                # if array sum is 0 and element at last one position
                if i==n-1 and s==0:
                    ans.append(0)
                elif s!=0:
                    ans.append(0-s) 
                    s=0
                elif s==0:
                    ans.append(i)
                    s=i
            return ans
