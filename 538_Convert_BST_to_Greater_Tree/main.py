# Given a Binary Search Tree (BST), convert it to a Greater Tree 
# such that every val of the original BST is changed to the original val 
# plus the sum of all keys greater than the original val in BST.
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# 
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstConverter(self, root):
        if root:
            self.bstConverter(root.right)
            root.val += self.addend
            self.addend = root.val
            self.bstConverter(root.left)
        return

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.addend = 0
        self.bstConverter(root)
        return root
       
