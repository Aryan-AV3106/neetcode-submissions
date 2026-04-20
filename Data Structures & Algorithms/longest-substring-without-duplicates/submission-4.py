class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxs = 0
        win = set()
        while r < len(s):
            
            while s[r] in win:
                win.remove(s[l])
                l+=1
            win.add(s[r])
            maxs=max(maxs,len(win))
            r+=1
            
        return maxs