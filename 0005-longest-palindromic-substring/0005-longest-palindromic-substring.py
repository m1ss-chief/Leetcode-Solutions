class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_s = ""
        if n == 1:
            return s
        for i in range(n):
            sub_s = s[i]
            for j in range(i+1,n):
                sub_s += s[j]
                if sub_s == sub_s[::-1] and len(max_s) < len(sub_s):
                    max_s = sub_s
            sub_s = ""
        return max_s if max_s != "" else s[0]
                
                


        