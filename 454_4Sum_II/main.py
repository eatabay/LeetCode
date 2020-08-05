# Given four lists A, B, C, D of integer values, 
# compute how many tuples (i, j, k, l) exist such that 
# A[i] + B[j] + C[k] + D[l] = 0 (zero).
# 
# All A, B, C, D have same length 'N', where 0 ≤ N ≤ 500.
# All integers are in the range of -2^28 to 2^28 - 1.
# The result is guaranteed to be at most 2^31 - 1.
# 
# Example:
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#

# Reword:
# - Find how many distinct combinations of i, j, k, l exist such that
#   A[i] + B[j] + C[k] + D[l] = 0

import collections

class Solution(object):
    def fourSumCountRef(self, A, B, C, D):

        # produce hash table of (a+b):count(a+b) pairs
        # (i.e., "x many of this total, y many of that total, etc.")
        #
        # important: Counter objects *return a zero count for missing items*
        # (instead of raising KeyError - like vanilla dict's)
        AB = collections.Counter(a+b for a in A for b in B)

        # find counts of (a+b) sums we could return to "0" by
        # 'adding' (c+b), and sum said counts
        return sum(AB[-c-d] for c in C for d in D)

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0

        for _, a_v in enumerate(A):
            for _, b_v in enumerate(B):
                for _, c_v in enumerate(C):
                    for _, d_v in enumerate(D):
                        if a_v + b_v + c_v + d_v  == 0:
                            count += 1

        return count

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [ 0, 2]

# A = [-8,-7,-14,-5,5,-24,-16,-24,-23,6,3,-26,-10,-14,-22,-11,-30,-2,-15,-18,-31,-1,-16,-22,-23,-24,-22,-16,-24,-15,-21,-18,-8,-7,7,-20,-32,-16,-24,5,3,-31,-18,2,-2,-11,-21,-26,-15,-14,1,10,0,-2,2,-10,3,-12,-10,-30,8,-31,2,-2,-4,-17,-24,-25,6,-11,-4,-29,5,-20,-16,-23,2,-27,6,-10,-2,-29,-15,9,-13,-20,8,-2,-17,6,-5,-26,6,-9,-29,-32,-27,-20,-7,-28]
# B = [-9,-6,-6,-24,-4,-25,0,-17,1,-10,-18,4,1,8,-28,3,8,4,-18,-18,-10,0,1,-23,-10,-8,-18,-13,-30,-8,-24,1,-24,5,-15,-19,-6,-7,2,-10,-24,-9,-15,-2,-28,-3,-24,7,-22,-9,-18,-4,-5,-28,-5,-22,-31,-2,0,-20,-9,-14,-32,-12,8,-22,-15,4,-9,-26,2,-5,-20,-13,-12,-13,-20,-8,-32,6,-4,-29,-5,4,-21,-13,-26,5,6,-25,-31,-15,10,3,5,5,-10,1,-7,8]
# C = [-6,6,-14,0,-2,-7,-16,0,-25,-28,0,0,-18,-15,4,-7,-26,-21,-3,-5,9,-14,6,-5,-26,-25,-27,-1,10,-13,7,-2,1,6,-12,7,-24,9,5,-27,8,-3,-12,-31,-27,-9,-10,-8,-27,-2,-20,-27,-13,0,8,-1,-25,0,10,-14,-23,-2,5,-28,-22,5,-12,-14,-15,8,-9,-6,-9,-22,-10,-31,-9,-24,-16,-13,-26,-5,-32,-29,9,-3,-10,8,-15,-31,-5,-18,5,-20,-2,10,-18,3,-1,-31]
# D = [-5,4,-4,-20,-32,7,-12,-15,-26,-15,6,2,-24,-14,-31,-11,-29,-5,-1,5,-29,-1,-26,-17,-12,-14,-12,6,-28,-28,9,-29,-22,-1,-31,1,-4,-24,-25,-18,8,-21,-29,0,5,-21,-10,-4,-25,-15,-32,-29,-15,-31,-25,6,-30,-23,7,-6,4,-32,9,-11,7,3,-21,-30,-25,-1,-13,-11,-24,-27,-12,-24,-27,-22,-31,-4,-20,-31,7,2,-25,-3,-12,-24,10,10,-9,-17,-22,-1,-16,-11,6,10,-20,5]

sln = Solution()
print(f'A[] = {A}')
print(f'B[] = {B}')
print(f'C[] = {C}')
print(f'D[] = {D}')
print(sln.fourSumCountRef(A, B, C, D))

