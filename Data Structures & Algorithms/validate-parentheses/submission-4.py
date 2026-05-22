class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for ch in s:
            if ch in open_to_close:
                stack.append(ch)
            else:
                if len(stack) == 0 or open_to_close[stack.pop()] != ch:
                    return False

        return not len(stack)