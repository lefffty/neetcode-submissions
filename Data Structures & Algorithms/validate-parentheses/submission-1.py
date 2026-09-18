class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        
        stack = deque()
        closing_parentheses = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        i = 0

        while i != n:
            if s[i] in closing_parentheses:
                if not stack or closing_parentheses[s[i]] != stack.popleft():
                    return False
                i += 1
            else:
                stack.appendleft(s[i])
                i += 1

        return True if not stack else False