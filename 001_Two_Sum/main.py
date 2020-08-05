import timeit

def twoSumNaive(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    pairs.append((i,j))
    return pairs

def twoSumBest(nums, target):
    ht = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in ht:
            return [ht[comp], i]
        ht[num] = i
    return []

nums = [3,7,3]
target = 6
# print(nums)
# print(twoSumNaive(nums, target))
twoSumBest(nums, target)
