class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        prevSum = nums[0]
        for i in range(1, len(nums)):
            prevSum = max(prevSum + nums[i], nums[i])
            maxSum = max(prevSum, maxSum)
        
        return maxSum
