# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
# 
# Example 1:
# 
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 
# Example 2:
# 
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix[0])
        
        rows,cols = set(),set()
        for r,row in enumerate(matrix):
            for col in range(len_row):
                if not row[col]:
                    rows.add(r)
                    cols.add(col)

        print(rows)
        print(cols)

        for r in rows:
            for c in range(len(matrix[r])):
                print(f'matrix[{r}][{c}] = 0')
                matrix[r][c] = 0

        for r in range(len(matrix)):
            for c in cols:
                matrix[r][c] = 0

        print(matrix)

        return

M1 = [ [1,1,1], [1,0,1], [1,1,1] ]
M2 = [ [0,1,2,0], [3,4,5,2], [1,3,1,5] ]
M3 = [ [1,0,3] ]
sln = Solution()
sln.setZeroes(M3)
