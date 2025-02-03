class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        for i, val in enumerate(nums):
            if val in visited and abs(visited[val] - i) <= k:
                return True
            visited[val] = i
        
        return False