class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap={}

        for char in allowed:
            hashmap[char]=1
        
        ans=0
        for word in words:
            f=False
            for c in word:
                if hashmap.get(c):
                    f=True
                else:
                    f=False
                    break
            
            if f: ans+=1
        
        return ans
