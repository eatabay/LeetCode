# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# Example 2:
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest_substring = 0
        len_s = len(s)

        for start_idx in range(0, len_s):
            stop_idx = start_idx + 1
            while stop_idx < len_s and s[stop_idx] not in s[start_idx:stop_idx]:
                stop_idx += 1
            substr_len = stop_idx - start_idx
            if substr_len > longest_substring:
                longest_substring = substr_len

        return longest_substring

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring(' '))
print(s.lengthOfLongestSubstring('au'))
print(s.lengthOfLongestSubstring('helop'))



