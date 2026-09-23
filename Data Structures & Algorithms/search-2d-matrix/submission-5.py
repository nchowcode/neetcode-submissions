class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search works on a sorted list.
        
        l = 0
        r = len(matrix) - 1

        while l <= r:
            middle = (l + r) // 2 
            # print(f"accessing.. {middle}, {matrix[middle][-1]}")
            if matrix[middle][-1] > target:
                r = middle - 1
            elif matrix[middle][-1] < target:
                l = middle + 1
            else:
                return True

        # print(matrix[l])
        # print(f"expected: {matrix[0]}")
        # row is now found
        if l == len(matrix):
            return False
            
        # print(l)
        nl = 0
        nr = len(matrix[l]) - 1

        while nl <= nr:
            middle = (nl + nr) // 2
            if matrix[l][middle] > target:
                nr = middle - 1
            elif matrix[l][middle] < target:
                nl = middle + 1
            else:
                return True

        return False