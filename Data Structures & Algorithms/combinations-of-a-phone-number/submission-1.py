from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        path = []
        res = []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        visited = set()
        # all possible combinations are in the mapping
        # when we start on number 1, we go to mapping, for each in there... we need to iter?
        # is this even back tracking? it looks like a double for loop...

        # visited set? so when we look at 3.. we dont go over again?
        # or maybe add the curr letter in path and then queue up the next ones?
        # then we need to pop it after?

        def dfs(i):
            # base case -> 4 == 4
            if i == len(digits):
                if path:
                    res.append("".join(path))
                return

            currentDigit = digits[i] # ie 3
            # 3 : [d,e,f]
            for letter in mapping[currentDigit]:
                path.append(letter)
                dfs(i + 1)
                path.pop()
            
            return

        dfs(0)
        return res
