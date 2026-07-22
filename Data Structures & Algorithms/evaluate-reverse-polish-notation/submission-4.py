class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        for ch in tokens:
            if ch not in operands:
                stack.append(int(ch))
            else:
                x, y = stack.pop(), stack.pop()
                if ch == "+":
                    val = x + y
                elif ch == "-":
                    val = y - x
                elif ch == "*":
                    val = y * x
                else:
                    val = int(y / x)
                stack.append(val)
        return stack.pop()
