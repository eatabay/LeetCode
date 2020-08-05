import random

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = [x for x in A if x%2 == 1]
        evens = [x for x in A if x%2 == 0]
        B = []
        for i in range(len(odds)):
            B.extend([evens[i], odds[i]])
        return B

A = [x for x in range(20)]
random.shuffle(A)
print(A)
sln = Solution()
sln.sortArrayByParityII(A)
