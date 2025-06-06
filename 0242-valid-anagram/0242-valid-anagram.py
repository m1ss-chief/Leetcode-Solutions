class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        flag = True
        s_s = list(s)
        s_s.sort()
        
        t_s = list(t)
        t_s.sort()
        for i in range(len(s)):
            if s_s[i] != t_s[i]:
                flag = False
        return flag
        
        