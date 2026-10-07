class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Sorted list, so we do binary search
        # First, we want to find the correct row
        row_l = 0
        row_r = len(matrix) - 1
        target_row = None
        while row_l <= row_r:
            row_mid = (row_l + row_r) //2
            # print(row_mid, row_r, row_l)
            if target < matrix[row_mid][0]:
                row_r = row_mid - 1
            #if there are only two possible rows, row must be left one
            elif target > matrix[row_mid][-1]:
                row_l = row_mid + 1
            else:
                target_row = row_mid
                break
        if target_row == None:
            return False
        #Repeat to find correct position within the row
        left = 0
        right = len(matrix[target_row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[target_row][mid]:
                return True
            elif target < matrix[target_row][mid]: 
                right = mid - 1
            else:
                left = mid + 1
        return False
