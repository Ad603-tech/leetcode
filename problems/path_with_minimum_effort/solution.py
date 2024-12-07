class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]

        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]

        while pq:
            r, c, effort = heapq.heappop(pq)

            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and  0 <= nc < cols:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (nr, nc, new_effort))
        
        return 0