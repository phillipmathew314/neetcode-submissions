class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "*":
                result = num1 * num2
            elif token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "/":
                result = int(num1 / num2)

            stack.append(result)
        
        return stack[-1]


# [10, 6, 9, 3]
# [10, 6, 12]
# [10, 6, 12, -11]
# [10, 6, -132]
# [10, 0]
# [0]
# [17, 5]
# 22