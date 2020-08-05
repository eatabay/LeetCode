# Given an integer array with no duplicates, 
# a "maximum" tree building on this array is defined as follow:
# 
# - The root is the maximum number in the array.
# - The left subtree is the maximum tree constructed from left subarray delimited by the maximum number.
# - The right subtree is the maximum tree constructed from right subarray delimited by the maximum number.
# 
# Construct the maximum tree of the given array and output the root node of this tree.
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}\n\tleft:{self.left}\n\tright:{self.right}'

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        # NTS: Mine was "okay"; but this one - using max() and <list>.index() - 
        # was faster.
        max_num = max(nums)
        max_idx = nums.index(max_num)

        max_node = TreeNode(max_num)
        max_node.left = self.constructMaximumBinaryTree(nums[0:max_idx])
        max_node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return max_node

    @staticmethod
    def traverseMaximumBinaryTree(root):
        childQueue = []

        node = root
        while node:
            print(node)
            if node.left:
                childQueue.append(node.left)
            if node.right:
                childQueue.append(node.right)
            try:
                node = childQueue.pop(0)
            except:
                break

        return


nums = [3,2,1,6,0,5]
sln = Solution()
theMBT = sln.constructMaximumBinaryTree(nums)
sln.traverseMaximumBinaryTree(theMBT)


