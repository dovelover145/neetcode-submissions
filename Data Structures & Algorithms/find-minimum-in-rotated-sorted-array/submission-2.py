class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search_lower_bound(nums):
            l, r = 0, len(nums) - 1

            while l < r:
                m = l + (r - l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                elif nums[m] < nums[r]:
                    r = m
                else: # If they're equal, then reduce the search space by 1
                    r -= 1 
            
            return nums[l]
        
        return binary_search_lower_bound(nums)