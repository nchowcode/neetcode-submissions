class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res is the days the temperature survived being the hottest. if 0 = hottest in the future

        res = [0] * len(temperatures)
        stack = [] # store (temp, index)

        for idx, val in enumerate(temperatures):
            if not stack:
                stack.append((val, idx))
            else:
                if stack[-1][0] >= val:
                    stack.append((val, idx))
                else:
                    while stack and stack[-1][0] < val:
                        poppedVal = stack.pop()
                        temp, index = poppedVal
                        res[index] = idx - index
                    stack.append((val, idx))

        return res