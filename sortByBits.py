class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        t={};
        res=[];

        for i in range(len(arr)):
            if bin(arr[i]).count('1') in t:
                t[bin(arr[i]).count('1')].append(arr[i]);
            else:
                t[bin(arr[i]).count('1')]=[arr[i]];
        print(t);

        for i in sorted(t.keys()):
            res+=sorted(t[i]);
        
        return res;
