class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        remove = set(stack)

        ans = []

        for i, ch in enumerate(s):
            if i not in remove:
                ans.append(ch)

        return "".join(ans)