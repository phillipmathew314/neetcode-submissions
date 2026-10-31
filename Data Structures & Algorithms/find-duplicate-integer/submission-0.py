class Solution:

    # approach 1: sort, binary search - O(nlogn), O(1)
    # approach 2: hashmap - O(n), O(n)
    # approach 3: modify nums itself by swapping with the index the number is supposed to be at (sorting it). first one out of place is the dupe - O(n), O(1)

    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                idx_to_swap = nums[i] - 1
                if nums[idx_to_swap] == idx_to_swap + 1:
                    return nums[idx_to_swap]
                else:
                    nums[i], nums[idx_to_swap] = nums[idx_to_swap], nums[i]