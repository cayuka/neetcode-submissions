# [2,4,-4,-1]

# 0
#stack []

# 1
# [2]

# 2
# [2, 4]

# 3 a = -4
# [2, ]

# 4 a = -1 
# [2]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # [2,4,-4,-1]

        for a in asteroids: # 2
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                if diff < 0:
                    stack.pop()
                if diff > 0:
                    a = 0
                if diff == 0:
                    a = 0
                    stack.pop()

            if a != 0:
                stack.append(a)

        return stack
