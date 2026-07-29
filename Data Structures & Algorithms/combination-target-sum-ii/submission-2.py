class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index: int, targ: int, path: list):
            if index >= len(candidates) or targ < 0:
                return
            
            if targ - candidates[index] == 0:
                path.append(candidates[index])
                res.append(path[:])
                path.pop()
            
            if targ - candidates[index] > 0:
                path.append(candidates[index])
                backtrack(index + 1, targ - candidates[index], path)
                path.pop()
            
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            if targ > 0:
                backtrack(index + 1, targ, path)

        backtrack(0, target, [])
        return res
