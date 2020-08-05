# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output: 321
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# Note:
# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function 
# returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # check sign
        negative = (x < 0)
        # clear sign (i/a) & convert to string
        str_abs_x = str(abs(x))
        # reverse
        rvrs_str_abs_x = str_abs_x[::-1]
        # convert to integer
        int_rvrs_abs_x = int(rvrs_str_abs_x)
        # negate (i/a)
        int_rvrs_x = (0 - int_rvrs_abs_x) if negative else int_rvrs_abs_x
        # ship it
        return int_rvrs_x

    # Mine is faster (24ms); but this one's much cleaner.
    def reverseRef(self, x):
        x = cmp(x,0)*int(str(abs(x))[::-1])
        if (x < -2**31) | (x > 2**31 - 1):
            return 0
        else:
            return x
