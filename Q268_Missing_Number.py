class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for n in range(len(nums)):
            if nums[n] != n:
                return n
        return len(nums)

#List always starts from 0, use that as the base, then sort the list and use range because +1 in range will equal actual number because indexing starts from 0
