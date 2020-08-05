# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the result in a linked list of similar structure.
# 
# You may assume the two numbers do not contain any leading zero, except the number "0" itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##########
# My approach...
#
# 1) Start "easy" - let's add "123" to "456" (i.e., same length, no carry).
#
# Things to consider:
# - carry (i.e., sum at any given digit i = l1[i] + l2[i] + carry)
# - if len(l1) != len(l2)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def listToInt(l):
    l_arr = []
    while l:
        l_arr.append(l.val)
        l = l.next
    l_arr.reverse()
    c_str = ''.join(map(str,l_arr))
    return int(c_str)

def intToList(num):
    # convert number into digit array
    num_array = [int(d) for d in str(num)]

    # build ListNode list out of digit array
    l = None
    for num in num_array:
        new_node = ListNode(num)
        if not l:
            l = new_node
        else:
            new_node.next = l
            l = new_node

    return l

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    result = listToInt(l1) + listToInt(l2)
    r_arr = intToList(result)

    return r_arr

def traverse(listNodeList):
    traverse = listNodeList
    while traverse:
        print(f'{traverse.val}',end=' -> ')
        traverse = traverse.next
    print("")
    return

l1_raw = int(input("Enter 1st number: "))
l2_raw = int(input("Enter 2nd number: "))

l1 = intToList(l1_raw)
l2 = intToList(l2_raw)

traverse(l1)
traverse(l2)

result = addTwoNumbers(l1, l2)
traverse(result)

