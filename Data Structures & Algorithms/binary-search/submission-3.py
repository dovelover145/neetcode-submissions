class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid_index = (len(nums) - 1) // 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] < target:
            res = self.search(nums[mid_index + 1:], target)
            return mid_index + 1 + res if res >= 0 else -1
        else:
            return self.search(nums[:mid_index], target)