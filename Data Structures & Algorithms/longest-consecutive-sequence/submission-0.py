class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = set(nums)
        res = 1
        for num in nums:
            left = right = 1
            num_res = 1
            while num-left in d or num+right in d:
                if num-left in d:
                    d.remove(num-left)
                    num_res += 1
                    left += 1
                if num+right in d:
                    d.remove(num+right)
                    num_res += 1
                    right += 1
            res = max(res, num_res)
        
        return res