class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for s in strs:
            temp="".join(sorted(s))
            if dic.get(temp):
                dic[temp].append(s)
            else:
                dic[temp]=[s]
        return dic.values()
