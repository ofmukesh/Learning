class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        need_map, window = {}, {}

        for i in t:
            need_map[i] = 1 + need_map.get(i, 0)
        
        have = 0
        need = len(need_map)

        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in need_map and window[s[r]] == need_map[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in need_map and window[s[l]] < need_map[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res[0], res[1]
        
        return s[l:r + 1] if resLen != float("infinity") else ""

                
