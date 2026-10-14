class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing=set()
        for i in range(len(nums)):
           missing.add(nums[i])
        for i in range(len(nums)+1):
            if i not in missing:
             return i
        