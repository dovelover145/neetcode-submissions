class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # Stores pairs of (i, h)

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                stack_h, stack_i = stack.pop()
                res_area = (i - stack_i) * stack_h
                max_area = max(max_area, res_area)
                start = stack_i
            stack.append((h, start))
        
        while stack:
            stack_h, stack_i = stack.pop()
            res_area = (len(heights) - stack_i) * stack_h
            max_area = max(max_area, res_area)
        
        return max_area