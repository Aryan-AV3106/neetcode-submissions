class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 1
        biggest = 0
        for num in s:
            if num-1 not in s:
                while num+1 in s:
                    count+=1
                    num+=1

                if biggest < count:
                    biggest = count
                count = 1
        return biggest