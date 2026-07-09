class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")":"(" , "]":"[", "}":"{" }
        for st in s:
            if st in mapping:
                if stack and stack[-1] == mapping[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        if not stack:
            return True
        else:
            return False
        