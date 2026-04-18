class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d ={}
        for strd in strs:
            s = str(sorted(strd))
            if s in d:
                d[s] = d[s] + [strd]
            else:
                d[s] = [strd]

        
        return list(d.values())