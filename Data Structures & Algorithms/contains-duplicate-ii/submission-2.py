class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        m = set()

        for i in range(k + 1):
            if nums[i] in m:
                return True
            m.add(nums[i])

        for i in range(k + 1, len(nums)):
            m.remove(nums[i-k-1])
            if nums[i] in m:
                return True
            m.add(nums[i])
        
        return False