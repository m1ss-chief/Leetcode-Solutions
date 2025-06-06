class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new = ""
        n = len(s)
        if s == goal:
            return True
        for i in range(1,n):
            new = s[i:]+s[:i]
            if new == goal:
                return True
            new = ""
        return False
        