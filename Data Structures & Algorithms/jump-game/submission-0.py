class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_spot = 0
        i = 0
        while i <= max_spot:
            max_spot = max(max_spot, i + nums[i])
            i += 1
            if max_spot >= len(nums) - 1:
                return True

        return False