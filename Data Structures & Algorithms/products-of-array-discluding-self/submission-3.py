class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        suff = 1 
        result = [0]*len(nums)
        
        for itr in range(len(nums)):
            result[itr] = pre
            pre *= nums[itr]
        
        for itr in range(len(nums)-1,-1,-1):
            result[itr] *= suff
            suff *= nums[itr]
        return result