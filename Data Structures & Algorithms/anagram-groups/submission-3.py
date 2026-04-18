class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for strd in strs:
            count= [0]*26 # array for all the alphabets

            for c in strd:
                count[ord(c)-ord("a")] +=  1

            key = tuple(count)

            if key not in d:
                d[key] = []
            
            d[key].append(strd)

        return list(d.values())
