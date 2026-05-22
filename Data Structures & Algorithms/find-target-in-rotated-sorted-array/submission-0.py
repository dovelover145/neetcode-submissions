class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: # The left portion of the array is sorted (as the pivot is located in the other portion)
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: # Right portion is sorted
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1