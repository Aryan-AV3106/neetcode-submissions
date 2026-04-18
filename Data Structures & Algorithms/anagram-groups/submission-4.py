class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d ={}
        for strd in strs:
            s = str(sorted(strd))
            if s not in d:
                d[s] = []
            d[s].append(strd)

        return list(d.values())