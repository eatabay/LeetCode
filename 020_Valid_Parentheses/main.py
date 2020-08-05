# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# Input: "()"
# Output: true
# 
# Example 2:
# 
# Input: "()[]{}"
# Output: true
# 
# Example 3:
# 
# Input: "(]"
# Output: false
# 
# Example 4:
# 
# Input: "([)]"
# Output: false
# 
# Example 5:
# 
# Input: "{[]}"
# Output: true

class Stack(object):
    def __init__(self):
        self.stack_list = []
        return

    def push(self, item):
        self.stack_list.append(item)
        return

    def pop(self):
        try:
            top = self.stack_list.pop()
        except:
            top = False
        return top

class Solution(object):
    @staticmethod
    def isMatch(parensA, parensB):
        if parensA == '[':
            return parensB == ']'
        elif parensA == '(':
            return parensB == ')'
        elif parensA == '{':
            return parensB == '}'
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match_dict = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in '[({':
                stack.append(c)
            else:
                try:
                    open_c = stack.pop()
                except:
                    return False

                if match_dict[open_c] != c:
                    return False
        
        return len(stack) == 0

sln = Solution()
test_v = ["()", "(){}[]", "(]", "([)]", "{[]}", "", "{", "}"]
for test_str in test_v:
    print(f'{test_str} :\t{sln.isValid(test_str)}')


