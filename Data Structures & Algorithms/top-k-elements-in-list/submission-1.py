class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            d[num] = d.get(num,0)+1

        sorted_dict = sorted(d.items(), key = lambda item:item[1],reverse = True)

        sol = []
        i = 0
        while i < k:
            sol.append(sorted_dict[i][0])
            i+=1
        
        return sol