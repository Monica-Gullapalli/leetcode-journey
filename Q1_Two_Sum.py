class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Need to use dictionary because the values you are trying to assign is a key-value format where you assign value and also add index as per line 10.
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return (d[diff], i)
            else:
                d[nums[i]] = i 
                #here's where you are assigning value of nums at i to ith index in dict d