class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            temp = two
            two = max(n + one, two)
            one = temp
        return two