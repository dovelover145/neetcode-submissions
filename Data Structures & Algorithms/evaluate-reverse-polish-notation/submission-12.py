class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                op_2, op_1 = stack.pop(), stack.pop()
                stack.append(op_1 - op_2)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                op_2, op_1 = stack.pop(), stack.pop()
                stack.append(int(op_1 / op_2))
            else:
                stack.append(int(token))
        
        return stack.pop()