class Solution(object):
    def toLowerCase(self, s):
        """
        :type str: s
        :rtype: str
        """
        out = ''
        for c in s:
            out += chr(ord(c) + 32) if ('A' <= c and c <= 'Z') else c
        return out

sln = Solution()
print(sln.toLowerCase("hEllo"))

