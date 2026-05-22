class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # The number of rows (where there is at least one)
        n = len(matrix[0]) # The number of columns
        l = 0
        r = m * n - 1

        while l <= r:
            midpoint = l + (r - l) // 2 # To prevent integer overflow
            i = midpoint // n
            j = midpoint % n
            if matrix[i][j] > target:
                r = midpoint - 1
            elif matrix[i][j] < target:
                l = midpoint + 1
            else:
                return True

        return False