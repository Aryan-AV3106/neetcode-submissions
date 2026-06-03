class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for word in strs:
            count = [0]*26    # an array that represents all the alphabets.


            for char in word:
                count[ord(char) - ord("a")] +=1
            key = tuple(count)    

            if key not in d:
                d[key] = []

            d[key].append(word)

        return list(d.values()
        )