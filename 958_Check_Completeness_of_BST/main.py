# Given a binary tree, determine if it is a complete binary tree.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, 
# is completely filled, and all nodes in the last level are as far 
# left as possible. It can have between 1 and 2h nodes inclusive 
# at the last level h.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}'

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    print(inputValues)
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def traverse(root):
    '''
    Performs inorder traversal of BST rooted at 'root'.
    Inorder traversal == Left-Root-Right
    '''
    if root:
        traverse(root.left)
        print(root)
        traverse(root.right)
    return

class Solution(object):
    # WHAAAT!??
    def isCompleteTreeRef(self, root):
        if not root:
            return True

        queue = [(root, 1)]
        i = 0
        while i < len(queue):
            node, pos = queue[i]
            i += 1
            if node:
                queue.append((node.left, 2 * pos))
                queue.append((node.right, 2 * pos + 1))

        return queue[-1][1] == len(queue)

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        currLevelList = []
        currLevelList.append(root)

        while currLevelList:
            print(f'currLevel : ' + str([f'{node}' for node in currLevelList]))
            levelHasNone = False
            if None in currLevelList:
                levelHasNone = True
                # walk the level in reverse -
                # we should not encounter any valid node
                # before encountering a None
                haveSeenValidNode = False
                for node in currLevelList[::-1]:
                    if node:
                        haveSeenValidNode = True
                    elif haveSeenValidNode:
                        return False
                if not haveSeenValidNode:
                    break

            # build the list for the next level
            nextLevelList = []
            for node in currLevelList:
                if node:
                    leftChild = node.left
                    rightChild = node.right
                    if rightChild and not leftChild:
                        # tree contains node with a right child
                        # but no left child; it cannot possibly be Complete
                        return False
                else:
                    leftChild = None
                    rightChild = None
                if levelHasNone and (leftChild or rightChild):
                    # tree has level that is not complete filled
                    # yet also nodes at the level; it cannot possibly be Complete
                    return False
                nextLevelList.extend([leftChild, rightChild])
            print(f'nextLevel : ' + str([f'{node}' for node in nextLevelList]))

            # proceed to next level
            currLevelList = nextLevelList

        return True

if __name__ == '__main__':
    in_str = "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]"
    bsTree = stringToTreeNode(in_str)
    traverse(bsTree)
    
    sln = Solution()
    print('Tree is {}Complete.'.format("" if sln.isCompleteTreeRef(bsTree) else "NOT "))
 
