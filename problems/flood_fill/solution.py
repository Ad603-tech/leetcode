class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        if image[sr][sc] == color:
            return image
        
        queue = deque()
        queue.append((sr, sc))


        pixel = image[sr][sc]
        image[sr][sc] = color
        

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == pixel:
                        image[nx][ny] = color
                        queue.append((nx, ny))
            
        return image
            