class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # the function
        def isPrefixAndSuffix(str1, str2):
            if len(str1)>len(str2): return False # return false if str1 is bigger than str1

            # if str1 is both a prefix and a suffix of str2 then return True
            if str2[0:len(str1)]==str1 and str1==str2[len(str2)-len(str1):]:
                return True
            
            # otherwise False
            return False
        
        # solution
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    count+=1

        return count
