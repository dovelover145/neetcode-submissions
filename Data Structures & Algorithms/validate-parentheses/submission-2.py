class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for i in range(len(s)):
            if s[i] in char_dict:
                stack.append(s[i])
            else:
                if len(stack) == 0 or char_dict[stack.pop()] != s[i]:
                    return False

        return not len(stack)    
