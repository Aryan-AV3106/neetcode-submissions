class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1

        sorted_d = sorted(d.items(),key = lambda item: item[1],reverse = True)

        result = []
        for i in range(len(sorted_d)):
            if i < k:
                result.append(sorted_d[i][0])
            
        return result