# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def isPalindrome(self, s):
        print(f'isPalindrome: checking \"{s}\"...')
        if not len(s):
            return True
        if len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPalindromeLen = 0
        maxPalindrome = ''

        for headIdx in range(len(s)):
            tailIdx = len(s) - 1
            while headIdx < tailIdx and s[headIdx] != s[tailIdx]:
                tailIdx -= 1
            if headIdx == tailIdx:
                continue
            if self.isPalindrome(s[headIdx:tailIdx+1]):
                thisPalindromeLen = (tailIdx + 1) - headIdx
                if thisPalindromeLen > maxPalindromeLen:
                    maxPalindromeLen = thisPalindromeLen
                    maxPalindrome = s[headIdx:tailIdx+1]

        if maxPalindromeLen:
            print(maxPalindrome + "(" + str(maxPalindromeLen) + ")")

        return maxPalindromeLen

sln = Solution()
print(sln.longestPalindrome("helleeo"))
print(sln.longestPalindrome("efe"))
print(sln.longestPalindrome(""))
