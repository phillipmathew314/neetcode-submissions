class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        def findRectangleAreaLess(index, minHeight, area) -> int:
            while index >= 0 and heights[index] >= minHeight:
                area += minHeight
                index -= 1
            return area
        
        def findRectangleAreaMore(index, minHeight, area) -> int:
            while index < len(heights) and heights[index] >= minHeight:
                area += minHeight
                index += 1
            return area

        for mid in range(len(heights)):
            ans = max(ans, heights[mid] + findRectangleAreaLess(mid - 1, heights[mid], 0) + findRectangleAreaMore(mid + 1, heights[mid], 0))
            print(ans)
        return ans