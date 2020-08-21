class Solution:
    # Runtime: 172 ms, faster than 15.17%
    # Memory Usage: 15.6 MB, less than 38.75%
    def removeDuplicates(self, nums):
        numsLen = len(nums)

        # trivial case
        if numsLen < 2: return numsLen

        lastIdx = 0
        currIdx = 1
        while currIdx < numsLen:
            # this comparison is not necessary & slows the algo down ~50% (!)
            # (see removeDuplicatesFinal)
            if nums[lastIdx] == nums[currIdx]:
                currIdx += 1
            else:
                lastIdx += 1
                nums[lastIdx] = nums[currIdx]

        return lastIdx+1

    # Runtime: 84 ms, faster than 86.42%
    # Memory Usage: 15.7 MB, less than 14.36%
    def removeDuplicatesFinal(self, nums):
        numsLen = len(nums) 

        # trivial case
        if numsLen < 2: return numsLen

        lastIdx = 0 
        currIdx = 1
        while currIdx < numsLen: 
            if nums[lastIdx] != nums[currIdx]:
                lastIdx += 1
                nums[lastIdx] = nums[currIdx]
            currIdx += 1

        return lastIdx+1

# Quickie test:
testVectors = [[],[0],[0,0],[0,1],[0,0,1],[0,1,1],[0,0,1,1,1,2,2,3,3,4]]
for testVector in testVectors:
    print(f'testVector in  : {testVector}')
    mySolution = Solution()
    mySolutionResult = mySolution.removeDuplicatesFinal(testVector)
    print(f'testVector out : {testVector} (length {mySolutionResult})')
