class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        biggest = 0
        s = set(nums)
        for x in s:
            if x-1 not in s:
                while x+1 in s:
                    count +=1
                    x+=1
                if biggest < count:
                    biggest = count
                count = 1
        return biggest