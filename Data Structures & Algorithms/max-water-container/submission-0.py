class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights) - 1
        res = (right - left) * min(heights[left], heights[right])

        while left != right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            res = max(res, (right - left) * min(heights[left], heights[right]))
        
        return res
            