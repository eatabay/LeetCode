# Reverse bits of a given 32 bits unsigned integer.
# 
# Example 1:
# 
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents 
# the unsigned integer 43261596; so, return 964176192, whose binary representation 
# is 00111001011110000010100101000000.
# 
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # bits_n = format(n, '0>32b')
        # return int(bits_n[::-1],2)
        return int(format(n, '0>32b')[::-1],2)


sln = Solution()

print(sln.reverseBits(43261596))
