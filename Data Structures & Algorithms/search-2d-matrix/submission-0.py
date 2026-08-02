class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low, high =  0, len(matrix) - 1
        row = -1

        while low <= high:
            middle = (low + high) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
               row = middle
               break

            elif target < matrix[middle][-1]:
                high = middle - 1

            else:
                low = middle + 1

        if row == -1:
            return False

        low, high =  0, len(matrix[row]) - 1
        while low <= high:
            middle = (low + high) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        
        return False