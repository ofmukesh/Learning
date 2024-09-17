class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        tmp={}
        ans={}
         
        for word in s1.split(" ")+s2.split(" "):
            ans[word]=1
        
        for word in s1.split(" ")+s2.split(" "):
            if tmp.get(word):
                if ans.get(word):
                    del ans[word]
            tmp[word]=1

        return ans.keys()
