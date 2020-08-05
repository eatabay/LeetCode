# In a 2 dimensional array grid, each value grid[i][j] represents the height of
# a building located there. We are allowed to increase the height of any number
# of buildings, by any amount (the amounts can be different for different
# buildings). Height 0 is considered to be a building as well.
#
# At the end, the "skyline" when viewed from all four directions of the grid,
# i.e. top, bottom, left, and right, must be the same as the skyline of the
# original grid. A city's skyline is the outer contour of the rectangles formed
# by all the buildings when viewed from a distance. See the following example.
#
# What is the maximum total sum that the height of the buildings can be
# increased?
#
# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
#
# The grid after increasing the height of buildings without affecting
# skylines is:
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

class Solution(object):
    def maxIncreaseKeepingSkylineRef(self,grid):
        row_max, col_max = [max(row) for row in grid], [max(col) for col in zip(*grid)]
        return sum(min(row_max[row], col_max[col]) - grid[row][col] for col in range(len(grid[0])) for row in range(len(grid)))
        
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        print(f'Input: {grid}')

        maxIncrease = 0

        rowMaxima = [-1] * len(grid)
        columnMaxima = [-1] * len(grid[0])
        for rowIdx, row in enumerate(grid):
            rowMaxima[rowIdx] = max(row)
            for colIdx, colItem in enumerate(row):
                if columnMaxima[colIdx] < colItem:
                    columnMaxima[colIdx] = colItem

        print(f'rowMaxima = {rowMaxima}')
        print(f'columnMaxima = {columnMaxima}')

        for rowIdx, row in enumerate(grid):
            for colIdx, _ in enumerate(row):
                while row[colIdx] < min(rowMaxima[rowIdx], columnMaxima[colIdx]):
                    row[colIdx] += 1
                    maxIncrease += 1

        print(f'Output: {grid}')
        print(f'maxIncrease = {maxIncrease}')

        return maxIncrease

city = [ [1, 0, 0, 0],
         [0, 2, 0, 0],
         [0, 0, 3, 0],
         [0, 0, 0, 4],
         [5, 0, 0, 0],
         [0, 6, 0, 0] ]
sln = Solution()
sln.maxIncreaseKeepingSkyline(city)
