class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        curr, prev = 0, 0
        ans = 0
        for num in reversed(s):
            curr = roman[num]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans

        