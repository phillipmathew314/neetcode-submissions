class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0
        while i < len(nums) - 2:
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # print(left, right)
                if nums[left] + nums[right] > target:
                    while left != right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    while left != right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1

            while i < len(nums) - 3 and nums[i] == nums[i+1]:
                i += 1
            
            i += 1
        
        return res