class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0

            for i in range(len(nums)):
                temp = rob2
                rob2 = max(rob1 + nums[i], rob2)
                rob1 = temp
            
            return rob2
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))