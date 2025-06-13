class Solution:
    def reverseWords(self, s: str) -> str:
        # rev_sen = []
        # ans = []
        # n = len(s)
        # new = ""
        # for i in range(n):
        #     if s[i] != " ":
        #         new += s[i]
        #     else:
        #         rev_sen.append(new)
        #         new = ""
        #     if i == n-1:
        #         rev_sen.append(new)
        # for word in rev_sen:
        #     if word == "":
        #         continue
        #     else:
        #         ans.append(word)
        # ans = ans[::-1]
        # return " ".join(ans)
        words = s.split()
        words = words[::-1]
        return " ".join(words)


            
        