class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        total = 0
        res = [-1,-1]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in s:
                    res[0] = grid[row][col]
                s.add(grid[row][col])
                total += grid[row][col]
        
        expected = (len(grid)**2 * (len(grid)**2 + 1)) // 2
        res[1] = expected - total + res[0]
        return res