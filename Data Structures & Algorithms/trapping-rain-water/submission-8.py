class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0]*len(height)
        max_rights = [0]*len(height)

        max_lefts[0] = 0
        max_left = height[0]
        max_rights[-1] = 0
        max_right = height[-1]
        for i in range(1, len(height)):
            max_left = max(max_left, height[i-1])
            max_lefts[i] = max_left

            max_right = max(max_right, height[-i])
            max_rights[-i-1] = max_right

        trapped_water = 0
        for i in range(1, len(height) - 1):
            trapped_water += max(min(max_lefts[i], max_rights[i]) - height[i], 0)
        
        return trapped_water