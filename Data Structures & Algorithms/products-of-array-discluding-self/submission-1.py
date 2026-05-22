class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        cur_prod = 1
        for i in range(len(nums)):
            res[i] = cur_prod
            cur_prod *= nums[i]
        cur_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cur_prod
            cur_prod *= nums[i]
        return res