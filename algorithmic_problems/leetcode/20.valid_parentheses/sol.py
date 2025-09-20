class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if (top == "(" and c == ")") or \
                   (top == "[" and c == "]") or \
                   (top == "{" and c == "}"):
                    stack.pop()
                else:
                    return False
        return not stack
