# optimized using Frequency counting
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        dic={}

        for num in nums:
            if dic.get(num)!=None:
                idx=dic[num]+1
                if idx<len(ans):
                    ans[idx].append(num)
                else:
                    ans.append([num])
                dic[num]=idx
            else:
                ans[0].append(num)
                dic[num]=0
        return ans
        '''
        time complexity -> O(n)
        space complexity - > O(n)
        '''


# optimized using sorting 
# [note - to use solution, change class Solution2 -> Solution]
class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        nums.sort()

        j=0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                j+=1
            else:
                j=0

            if j<len(ans):
                ans[j].append(nums[i])
            else:
                ans.append([nums[i]])
        
        return ans
        '''
        time complexity -> O(nlog n)
        space complexity - > O(1) 
        '''




# brute force solution
# [note - to use solution, change class Solution1 -> Solution]
class Solution1:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        array_2d=[[]]

        for num in nums:
            i=0
            t=False
            for i in range(len(array_2d)):
                if num not in array_2d[i]:
                    array_2d[i].append(num)
                    t=True
                    break

            if not t:
                array_2d.append([num])
        
        return array_2d

        '''
        time complexity -> O(n*m)
        space complexity - > O(1)
        '''
