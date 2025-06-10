class Solution:
    def frequencySort(self, s: str) -> str:
        res = {}
        ans = ""
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = 1
            else:
                res[s[i]] += 1
        res = dict(sorted(res.items(),key=lambda item: item[1],reverse=True))
        print (res)
        for x in res:
            while res[x] != 0:
                ans += x
                res[x] -= 1

        return ans
        