# Merge two binary trees by "transposing" them into a new binary tree.
#
# The merge rule is: if two nodes overlap, then sum node values up as the new value of the merged node;
# otherwise, the "non-None" node will be used as the node of new tree.
# 
# Example 1:
# 
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
# 
#  
# 
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None

        val1 = t1.val if t1 else 0
        val2 = t2.val if t2 else 0

        new_node = TreeNode(valA, valB)
        new_node.left = self.mergeTrees(t1.left, t2.left)
        new_node.right = self.mergeTrees(t1.right, t2.right)

        return new_node

