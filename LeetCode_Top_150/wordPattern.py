class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s)!=len(pattern):
            return False

        hashmap={}
        occupied={}
        ans=""
        for i,word in enumerate(s):
            if hashmap.get(word):
                ans+=hashmap[word]
            else:
                hashmap[word]=pattern[i]
                if occupied.get(pattern[i]):
                    return False
                else:
                    occupied[pattern[i]]=1
                    ans+=hashmap[word]
        print(ans)
        return ans==pattern

