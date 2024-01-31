# optimized solution using stack  T.C-> O(n) & S.C->O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[(temperatures[-1],len(temperatures)-1)]
        temperatures[-1]=0

        for i in range(len(temperatures)-2,-1,-1):
            j=len(stack)-1
            while j>=0:
                if temperatures[i]>=stack[j][0]:
                    stack.pop()
                else:
                    break
                j-=1
            
            stack.append((temperatures[i],i))
            temperatures[i]=stack[j][1]-i
        
        return temperatures



'''
# brute force solution - TLE
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for i in range(len(temperatures)):
            f=False
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    f=True
                    break
            if f:
                temperatures[i]=j-i
            else:
                temperatures[i]=0
        return temperatures
'''
