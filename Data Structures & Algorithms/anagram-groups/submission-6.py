class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for strd in strs:
            count= [0]*26 # array for all the alphabets

            # at the index changing 0 to 1
            for c in strd:
                count[ord(c)-ord("a")] +=  1
            key = tuple(count)# making a key, list cannot be key

            # instead of if else 
            if key not in d:
                d[key] = []
            # its list so can append
            d[key].append(strd)
        return list(d.values())
