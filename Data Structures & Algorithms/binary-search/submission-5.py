class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid_index = (len(nums) - 1) // 2 # Don't need -1
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            return self.search(nums[:mid_index], target)
        else: # nums[mid_index] < target
            index = self.search(nums[mid_index + 1:], target)
            return mid_index + 1 + index if index >= 0 else index