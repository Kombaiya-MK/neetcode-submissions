class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for idx in range(len(s)):
            if s[idx] in [')', ']', '}'] and len(stack) < 1:
                return False
            if s[idx] == ')' and stack[-1] != '(':
                return False
            elif s[idx] == '}' and stack[-1] != '{':
                return False
            elif s[idx] == ']' and stack[-1] != '[':
                return False
            elif s[idx] in ['(', '{', '[']:
                stack.append(s[idx])
            else:
                stack.pop(-1)
        if len(stack) > 0:
            return False
        return True

            
                
        