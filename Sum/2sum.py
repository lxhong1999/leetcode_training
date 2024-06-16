class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target - nums[i]) != i:  
                ans.append(i)
                ans.append(nums.index(target - nums[i]))
                return ans
        