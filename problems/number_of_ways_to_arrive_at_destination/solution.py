class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        graph = defaultdict(list)
        for u, v, weights in roads:
            graph[u].append((v, weights))
            graph[v].append((u, weights))
        
        distances = [float('inf')] * n
        ways = [0] * n
        distances[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    ways[neighbor] = ways[current_node]
                    heapq.heappush(pq, (distance, neighbor))
                
                elif distance == distances[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[current_node]) % MOD

        return ways[n-1]        