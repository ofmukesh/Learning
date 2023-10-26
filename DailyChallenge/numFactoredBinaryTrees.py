class Solution:
    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        dct = {elem: 1 for elem in arr} # 
        for elem in arr:
            for factor in arr:
                # itrating these elements which index has less then then curr index
                if factor == elem:
                    break
                if elem % factor == 0 and elem // factor in dct:
                    dct[elem] += dct[factor] * dct[elem // factor]
        return sum(dct.values()) % (pow(10, 9) + 7)
