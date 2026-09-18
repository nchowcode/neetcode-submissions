class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pattern:
        # at any time: [1,2] -> operand = action on 2 numbers. pop them both out, push in new num.

        stack = []
        exitOp = ['+', '-', '*', '/']

        for token in tokens:
            if token in exitOp:
                res = 0
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                else:
                    res = int(left / right)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
        