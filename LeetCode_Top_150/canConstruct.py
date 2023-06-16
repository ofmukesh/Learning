class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}

        for i in magazine:
            hashmap[i]=1+hashmap.get(i,0)

        for c in ransomNote:
            if not hashmap.get(c):
                return False
            elif hashmap[c]<=0:
                return False
            hashmap[c]-=1

        return True
