class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 1 
        highest = 0
        for num in nums:
            if num-1 not in nums:
                while num+1 in nums:
                    count+=1
                    num+=1
                if count > highest:
                    highest = count
            count = 1
        return highest