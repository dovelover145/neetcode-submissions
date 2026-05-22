class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(nums):
            l, r = 0, len(nums) - 1
            res = nums[0]

            while l <= r:
                if nums[l] <= nums[r]: # This part is sorted, so there's no need to continue
                    res = min(res, nums[l])
                    break
                
                m = l + (r - l) // 2
                res = min(res, nums[m]) # Make sure not to exclude this (because of r = m - 1)

                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            return res
        
        def binary_search_lower_bound(nums):
            l, r = 0, len(nums) - 1

            while l < r: # < because <= causes an infinite loop (r = m assignment)
                m = l + (r - l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                elif nums[m] < nums[r]:
                    r = m
                else: # If they're equal, then reduce the search space by 1
                    r -= 1 
            
            return nums[l] # Or nums[r]
        
        fcn = 0

        match fcn:
            case 0:
                return binary_search(nums)
            case 1:
                return binary_search_lower_bound(nums)
            case _:
                return -1