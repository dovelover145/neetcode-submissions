class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) 
        l, r = 0, m * n - 1 

        while l <= r:
            m = l + (r - l) // 2 # To prevent integer overflow
            i, j = m // n, m % n 
            if matrix[i][j] > target:
                r = m - 1
            elif matrix[i][j] < target:
                l = m + 1
            else:
                return True

        return False