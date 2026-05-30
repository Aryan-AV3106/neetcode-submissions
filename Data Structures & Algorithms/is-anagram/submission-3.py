class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
        
        count = {}
        for i in s:
            count[i] = count.get(i,0)+1
        
        for x in t:
            if x in count:
                count[x] = count.get(x)-1
                if count[x] == 0:
                    count.pop(x)
            else:
                return False
        return True
        