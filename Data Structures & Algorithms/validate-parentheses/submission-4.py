class Solution:
    def isValid(self, s: str) -> bool:
        # stack perfect representation of pairs, [open:close]
        # if stack is not empty by end of it, then it is NOT valid, else it is perfectly balanced

        closeToOpen = {
            ')':'(',
            '}':'{', 
            ']' :'['
        }

        stack = []
        for char in s:
            if char in closeToOpen: # = exit
                if len(stack) == 0:
                    return False
                if stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return False if stack else True


