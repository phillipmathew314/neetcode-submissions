class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]].append(i)
                if abs(m[nums[i]][-1] - m[nums[i]][-2]) <= k:
                    return True
            else:
                m[nums[i]] = [i]
        return False