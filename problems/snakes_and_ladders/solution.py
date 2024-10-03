class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(square):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if row % 2 != (n % 2) else n - 1 - rem
            return row, col

        queue = deque([(1, 0)])
        visited = set()
        visited.add(1)

        while queue:
            square, moves = queue.popleft()
            if square == n*n:
                return moves

            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                row, col = get_position(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1
