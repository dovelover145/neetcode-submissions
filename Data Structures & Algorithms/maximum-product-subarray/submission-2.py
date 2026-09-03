class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxL, minL = 1, 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                maxL, minL = 1, 1
                if 0 > res:
                    res = 0
            else:
                if nums[i] > 0:
                    maxL, minL = max(maxL * nums[i], nums[i]), min(minL * nums[i], nums[i])
                else:
                    maxL, minL = max(minL * nums[i], nums[i]), min(maxL * nums[i], nums[i])
                if maxL > res:
                    res = maxL
        
        return res
        