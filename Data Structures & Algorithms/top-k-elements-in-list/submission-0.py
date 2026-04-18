class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d ={}

        for num in nums:
            d[num] = d.get(num,0) + 1
        
        sol = sorted(d.items(),key=lambda x: x[1], reverse=True)
        i =0
        a = []
        while i < k:
            a.append(sol [i][0])
            i+=1
        
        return a