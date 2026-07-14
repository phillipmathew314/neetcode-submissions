class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(heights)):
            index = i
            while len(stack) > 0 and heights[i] < stack[-1][0]:
                height, index = stack.pop()
                ans = max(ans, (i - index) * height)
                
            stack.append([heights[i], index])

        while len(stack) > 0:
            height, index = stack.pop()
            ans = max(ans, (len(heights) - index) * height)
        
        return ans