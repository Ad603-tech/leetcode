class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)
        p = [0, 0]

        for move in moves:
            if move == 'R':
                p[0] = p[0] + 1
            elif move == 'L':
                p[0] = p[0] - 1
            elif move == 'U':
                p[1] = p[1] + 1
            elif move == 'D':
                p[1] = p[1] - 1
             
        if p[0] == 0 and p[1] == 0:
            return True
        else:
            return False