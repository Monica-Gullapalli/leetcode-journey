class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        
        
#go through the whole list of nums and if a number is greater than or equal to the target then it will be inserted at the same index i.e it will get replaced with the target
#if none of the numbers are less than the target which means we dont need to go over the list one by one and we can just return the length which is the total number of indexes + 1
