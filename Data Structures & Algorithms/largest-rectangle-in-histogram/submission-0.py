class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (start, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                top_start, top_h = stack.pop()
                top_w = i - top_start
                max_area = max(max_area, top_h * top_w)
                start = top_start
            stack.append((start, h))

        while stack:
            top_start, top_h = stack.pop()
            top_w = len(heights) - top_start
            max_area = max(max_area, top_h * top_w)
        
        return max_area