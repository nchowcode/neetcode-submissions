class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # path step: to exclude or include curr number
        # we are building subset, only appending when valid,
        candidates.sort()
        res = []
        subset = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            
            if i == len(candidates) or remaining < 0:
                return

            # if subset and subset[-1] == candidates[i]: # prune
            #     return

            subset.append(candidates[i])
            
            # include current, go next
            dfs(i + 1, remaining - candidates[i])

            # exclude current, go next
            subset.pop()

            # ok... but where to start?
            nextIndex = i + 1
            while nextIndex < len(candidates):
                nextValue = candidates[nextIndex]
                currValue = candidates[i]
                if nextValue == currValue:
                    nextIndex += 1
                else:
                    break

            dfs(nextIndex, remaining)


        dfs(0, target)
        return res
            


            


            