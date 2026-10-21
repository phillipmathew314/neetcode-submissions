class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_right = [nums[0]]
        for i in range(1, len(nums)):
            from_right.append(nums[i] * from_right[i-1])
        
        from_left = [0] * len(nums)
        from_left[-1] = nums[-1]
        for i in range(2, len(nums)+1):
            from_left[-i] = nums[-i] * from_left[-i+1]
        
        res = [0] * len(nums)
        res[0] = from_left[1]
        res[-1] = from_right[-2]
        for i in range(1, len(nums)-1):
            res[i] = from_left[i+1]*from_right[i-1]
        
        return res