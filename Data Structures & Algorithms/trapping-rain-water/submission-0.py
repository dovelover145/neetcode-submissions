class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped_water = 0

        if n < 3:
            return trapped_water

        left_max = height[0]
        right_max = height[n - 1]
        left = 1
        right = n - 2
        while left <= right:
            if left_max < right_max:
                trapped_water += max(left_max - height[left], 0)
                left_max = max(left_max, height[left])
                left += 1
            else:
                trapped_water += max(right_max - height[right], 0)
                right_max = max(right_max, height[right])
                right -= 1

        return trapped_water
