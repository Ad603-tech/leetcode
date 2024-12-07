class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0 

        def bfs(start):
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbour in range(n):
                    if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                        visited[neighbour] = True
                        bfs(neighbour)
        
        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                bfs(i)
        
        return provinces