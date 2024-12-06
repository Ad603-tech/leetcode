class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Collision occurs
                if stack[-1] < -asteroid:
                    stack.pop()  # Right-moving asteroid explodes
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both explode
                break
            else:
                # No collision or the left-moving asteroid survives
                stack.append(asteroid)

        return stack
        