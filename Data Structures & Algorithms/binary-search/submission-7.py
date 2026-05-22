class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def iterative_binary_search(nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1
        
        sol_num = 0
        match sol_num:
            case 0:
                return iterative_binary_search(nums, target)