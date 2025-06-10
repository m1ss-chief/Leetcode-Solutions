class Solution:
    def maxDepth(self, s: str) -> int:
        count, depth = 0, 0
        n = len(s)
        for x in s:
            if x == '(':
                count += 1
                depth = max(count, depth)

            if x == ')':
                count -= 1
        return depth 
        