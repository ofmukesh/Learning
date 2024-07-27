#User function Template for python3

class Solution:
    def gcd(self,a,b):
        while a>0 and b>0:
            if a<b:
                b-=a
            else:
                a-=b
        if a<=0:
            return b
        return a
        
    def lcmAndGcd(self, A , B):
        gcd=self.gcd(A,B)
        lcm=lcm = (A*B)//gcd
        return [lcm,gcd]
        
