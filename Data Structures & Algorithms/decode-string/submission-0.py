class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                curStr = []
                while stack[-1] != "[":
                    curStr.append(stack.pop())
                digit = []
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit.append(stack.pop())
                curStr = curStr * int("".join(digit[::-1]))
                stack.append("".join(curStr[::-1]))
            else:
                stack.append(ch)

        return "".join(stack)