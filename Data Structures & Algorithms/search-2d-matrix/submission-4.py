class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approach 1: flatten everything into list and do binary search
        # approach 2: use modulo operator

        left = 0
        right = len(matrix)*len(matrix[0]) - 1

        while left < right:
            mid = (left + right) // 2
            midx = mid // len(matrix[0])
            midy = mid % len(matrix[0])
            print(left, right, mid, midx, midy)
            print(matrix[midx][midy])
            if matrix[midx][midy] > target:
                right = mid-1
            elif matrix[midx][midy] < target:
                left = mid+1
            else:
                return True
        
        finalx = left // len(matrix[0])
        finaly = left % len(matrix[0])
        return matrix[finalx][finaly] == target