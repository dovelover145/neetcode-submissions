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
        
        def recursive_binary_search(nums: List[int], target: int) -> int:
            if len(nums) == 0:
                return -1
            l, r = 0, len(nums) - 1
            m = l + (r - l) // 2
            if nums[m] > target:
                return recursive_binary_search(nums[:m], target)
            elif nums[m] < target:
                res = recursive_binary_search(nums[m + 1:], target)
                return res if res == -1 else (m + 1) + res
            else:
                return m
        
        def recursive_binary_search_2(nums: List[int], l: int, r: int, target: int) -> int:
            if l > r:
                return -1
            m = l + (r - l) // 2
            if nums[m] > target:
                return recursive_binary_search_2(nums, l, m - 1, target)
            elif nums[m] < target:
                return recursive_binary_search_2(nums, m + 1, r, target)
            else:
                return m
        
        def dumb_brute_force_search(nums: List[int], target: int) -> int:
            for i, n in enumerate(nums):
                if n == target:
                    return i
            return -1

        sol_num = 3
        match sol_num:
            case 0:
                return iterative_binary_search(nums, target)
            case 1:
                return recursive_binary_search(nums, target)
            case 2:
                return recursive_binary_search_2(nums, 0, len(nums) - 1, target)
            case 3:
                return dumb_brute_force_search(nums, target)