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
                current = s[i]
                if not stack:
                    return False
                upper = stack.popleft()
                if closing_parentheses[current] != upper:
                    return False
                i += 1
            else:
                stack.appendleft(s[i])
                i += 1

        if stack:
            return False

        return True