class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n <= 1:
            return [0]
        result = [0] * n
        stack = []

        for idx in range(n):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = idx - prev_day

            stack.append(idx)

        return result