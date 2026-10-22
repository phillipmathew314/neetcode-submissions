class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if stack and d[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0