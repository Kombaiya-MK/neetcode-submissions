class Solution:
    def simplifyPath(self, path: str) -> str:
        dic = path.split("/")
        stack = []
        # print(dic)

        for ch in dic:
            isAlive = True
            if ch == "..":
                if stack:
                    stack.pop()
                isAlive = False

            if ch == "":
                isAlive = False

            if isAlive:
                stack.append(ch)
            
        # if  not stack:
        #     return "/"
        return  "/" + "/".join(stack)
        