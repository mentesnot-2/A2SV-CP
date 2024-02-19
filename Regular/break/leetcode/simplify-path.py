class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path[1:]
        path = path.split("/")
        path = path[:len(path) - 1] if path[-1] == '' else path[: len(path)]
        stack = []
     
        for k in path:
            if k == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif k == "." or k == "":
                continue
            else:
                stack.append(k)
        
        res = "/".join(stack)
        return "/" + res