class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n,0,-1):
            # if int(num[i-1])%2 != 0:
            if num[i-1] in {'1','3','5','7','9'}:
                return num[:i]
                
        return ""
         
        