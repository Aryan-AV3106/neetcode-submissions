class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:

            c = [0]*26 # stores a list for numbers.

            for char in word:
                c[ord(char) - ord("a")] += 1 
            key = tuple(c)
            if key not in d:
                d[key] = []
            
            d[key].append(word)
        
        return list(d.values())