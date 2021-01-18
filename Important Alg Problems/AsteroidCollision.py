'''

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.

'''
class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids: return []
        stack = [asteroids[0]]

        for aster in asteroids[1:]:
            if aster > 0:
                stack.append(aster)
            else:
                while stack and (stack[-1] > 0 and stack[-1] < abs(aster)):
                    stack.pop()

                if not stack or stack[-1] < 0: stack.append(aster)
                elif  stack[-1] + aster == 0: stack.pop()

        return stack

sol = Solution()
print(sol.asteroidCollision([-5,10,-15,7,-8,-9,10,-5]))

