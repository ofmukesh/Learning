# use a set and a index pointer 
# remove duplicate elements 
# update ans by max of ans & length of substring without repeating chars 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        charSet=set()
        l=0

        for r in range(len(s)):

            # removing duplicate chars from charSet 
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            # adding current char to charSet set
            charSet.add(s[r])

            # updating ans by max of ans & length of substring without repeating chars 
            ans=max(ans,r-l+1)
        return ans
