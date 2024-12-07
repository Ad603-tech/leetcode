class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        distances = [[float('inf')] * n for _ in range(n)]
        distances[0][0] = 0
        pq = [(0, 0, 1)]

        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        while pq:
            r, c, path_length = heapq.heappop(pq)

            if r == n - 1 and c == n - 1:
                return path_length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and  0 <= nc < n and grid[nr][nc] == 0:
                    distance = path_length + 1
                    if distance < distances[nr][nc]:
                        distances[nr][nc] = distance
                        heapq.heappush(pq, (nr, nc, distance))
        
        return -1

        
        