class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for t in range(n):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                prev_t = stack.pop()
                answer[prev_t] = t - prev_t
            stack.append(t)
        
        return answer

        