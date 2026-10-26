class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ind = 0
        res = [0]*len(temperatures)
        for temp in temperatures:
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                res[i] = ind - i
            stack.append((temp, ind))
            ind += 1
        
        return res


        # stack = [(38, 1), (36, 3),]
        # res = [1, _, 1]