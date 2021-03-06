# Given an array of integers 'nums' and a positive integer 'k',
# find whether it's possible to divide this array into 'k' non-empty 
# subsets whose sums are all equal.
# 
# Example:
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide 'nums' into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

import itertools

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        return not (sum(nums) % k)

nums_true = [4,3,2,3,6,5,1]
nums_false = [2,2,2,2,3,4,5]
k = 4

sln = Solution()
print(sln.canPartitionKSubsets(nums, k))
