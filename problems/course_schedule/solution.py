class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0

        while queue:
            node = queue.popleft()
            visited_courses += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited_courses == numCourses
        